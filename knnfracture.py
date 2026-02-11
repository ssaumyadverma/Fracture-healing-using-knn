import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# Step 1: Load CSV Dataset
# -----------------------------
csv_file = "Femoral_Neck_BMD_Dataset.csv"   # fixed filename
df = pd.read_csv(csv_file)

# -----------------------------
# Step 2: Data Quality Checks
# -----------------------------
def check_nulls(df):
    null_report = df.isnull().sum()
    print("\nNull Check Report:\n", null_report)
    return null_report

def check_column_types(df):
    # Predefined expected types
    expected_types = {
        "Date": "object",        # will parse later if needed
        "Name": "object",
        "Age": "int64",
        "BMI": "float64",
        "Weight": "float64",
        "BMD": "float64",
        "T_Score": "float64",
        "Obesity": "object",
        "Patient_ID": "object"
    }
    type_report = {}
    for col, expected in expected_types.items():
        if col in df.columns:
            actual = str(df[col].dtype)
            type_report[col] = (actual == expected, actual, expected)
    print("\nColumn Type Report:\n", type_report)
    return type_report

def check_string_lengths(df):
    # Predefined string length rules
    string_rules = {"Patient_ID": 10, "Name": 50}
    length_report = {}
    for col, max_len in string_rules.items():
        if col in df.columns and df[col].dtype == "object":
            invalid = df[df[col].str.len() > max_len]
            length_report[col] = len(invalid)
    print("\nString Length Report:\n", length_report)
    return length_report

# Run checks
check_nulls(df)
check_column_types(df)
check_string_lengths(df)

# -----------------------------
# Step 3: Healing Days Logic
# -----------------------------
def healing_days(t_score):
    if t_score >= -1:
        return 49  # midpoint of 42–56
    elif t_score > -2.5:
        return 70  # midpoint of 56–84
    else:
        return 98  # midpoint of 84–112+

df["no_days_taken_to_heal"] = df["T_Score"].apply(healing_days)
df["healing_range"] = df["T_Score"].apply(
    lambda x: "42-56 days" if x >= -1 else "56-84 days" if x > -2.5 else "84-112+ days"
)

# -----------------------------
# Step 4: Feature Selection
# -----------------------------
df["Obesity"] = df["Obesity"].map({"Yes": 1, "No": 0})
X = df[["Age", "Weight", "BMD", "BMI", "Obesity"]].values
y = df["no_days_taken_to_heal"].values

# -----------------------------
# Step 5: Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -----------------------------
# Step 6: Build KNN Regressor
# -----------------------------
knn = KNeighborsRegressor(n_neighbors=5, metric="euclidean")
knn.fit(X_train, y_train)

# -----------------------------
# Step 7: Predict Healing Days
# -----------------------------
y_pred = knn.predict(X_test)

# -----------------------------
# Step 8: Evaluate
# -----------------------------
print("\nPredicted healing days:", y_pred[:10])
print("Actual healing days:", y_test[:10])
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# -----------------------------
# Step 9: X-ray Recommendation
# -----------------------------
def recommend_xray(days):
    if days <= 56:
        return "Recommend X-ray"
    elif days <= 84:
        return "Consider X-ray"
    else:
        return "Delay X-ray"

df["Xray_Recommendation"] = df["no_days_taken_to_heal"].apply(recommend_xray)

# -----------------------------
# Step 10: Save Cleaned Data
# -----------------------------
output_file = "Femoral_Neck_BMD_Dataset_clean.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned dataset with predictions and recommendations saved to {output_file}")
