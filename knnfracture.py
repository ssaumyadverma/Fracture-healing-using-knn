# Step 1: Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# Step 2: Load dataset
excel_file = "Femoral_Neck_BMD_Dataset.xlsx"   # replace with actual file path
sheet_name = "Sheet1"

# Read Excel and convert to CSV
df = pd.read_excel(excel_file, sheet_name=sheet_name)
csv_file = "Femoral_Neck_BMD_Dataset.csv"
df.to_csv(csv_file, index=False)
print(f"Converted {excel_file} (sheet: {sheet_name}) to {csv_file}")

# Reload CSV
df = pd.read_csv(csv_file)

# Step 3: Healing days logic
def healing_days(t_score):
    if t_score >= -1:
        return 49   # midpoint of 42–56
    elif t_score > -2.5:
        return 70   # midpoint of 56–84
    else:
        return 98   # midpoint of 84–112+

df["no_days_taken_to_heal"] = df["T_Score"].apply(healing_days)

# Step 4: Features + target
X = df[["Age", "Weight", "BMD", "BMI", "Obesity"]].values
y = df["no_days_taken_to_heal"].values

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: KNN regressor
knn = KNeighborsRegressor(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

# Step 7: Predictions
y_pred = knn.predict(X_test)

# Step 8: Evaluation
print("Predicted healing days:", y_pred[:10])
print("Actual healing days:", y_test[:10])
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# Step 9: Define function to recommend X-ray follow-up
def recommend_xray(healing_days):
    """
    Patients with shorter healing times (fracture likely healed)
    can be considered for X-ray confirmation.
    """
    if healing_days <= 56:
        return "Recommend X-ray"
    elif healing_days <= 84:
        return "Consider X-ray"
    else:
        return "Delay X-ray"

# Apply function to dataset
df["Xray_Recommendation"] = df["no_days_taken_to_heal"].apply(recommend_xray)

# Preview results
print(df[["T_Score", "no_days_taken_to_heal", "Xray_Recommendation"]].head())
