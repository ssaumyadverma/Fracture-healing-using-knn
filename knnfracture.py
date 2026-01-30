# Step 1: Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# Step 2: Load dataset (replace with actual path or URL)
# Example: downloaded CSV from Mendeley dataset
df = pd.read_csv("clinical_bmd_dataset.csv")

# Step 3: Generate healing days column based on BMD/T-score logic
# Formula: IF(T_score >= -1, "42-56 days", IF(T_score > -2.5, "56-84 days", "84-112+ days"))
def healing_days(t_score):
    if t_score >= -1:
        return 49   # midpoint of 42–56
    elif t_score > -2.5:
        return 70   # midpoint of 56–84
    else:
        return 98   # midpoint of 84–112+
        
df["no_days_taken_to_heal"] = df["T_Score"].apply(healing_days)

# Step 4: Select features (BMD + vitals)
X = df[["Age", "Weight", "BMD", "BMI", "Obesity"]].values
y = df["no_days_taken_to_heal"].values

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Build KNN regressor
knn = KNeighborsRegressor(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

# Step 7: Predict healing days
y_pred = knn.predict(X_test)

# Step 8: Evaluate
print("Predicted healing days:", y_pred[:10])
print("Actual healing days:", y_test[:10])
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
