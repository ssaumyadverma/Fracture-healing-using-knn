# Fracture-healing-using-knn
To take clinical data, consider Bone mass density and predict healing of a fracture based on the variables
Take BMD of patient and calculate the standard deviation from the other previously healed individual patient having similar or near about BMD in their case using K nearest neighbour algorithm.

Dependencies -
	1. Available open source dataset online.
	2. Different patients' individual body vitals.
	3. Extent and volume of data.

Objective - 
	1. To determine the healing days required to keep the plaster on and other supportive aids for the patient.
	2. Later stages to confirm palpation tests.

Definitions -

-----types of tests done by doctors before plaster is opened - visual inspection, palpation alias plp placeholder, circulation test, neurological checks, movement and function.
-----This palpation, or pressing, of the muscle is an important part of the diagnosis, as it helps to determine the extent and grade of the tear.
-----Columns in Dataset available
Sr. No |	Gender	| Age	| Height |	Weight |	BMD |	T_Score |	Z_Score |	Area |	BMC |	BMI |	Obesity | Group	| BFP	| STD


From <https://data.mendeley.com/datasets/kys6x6wykj/1/files/de8d831f-472e-409e-8bf4-4495fdc309d7> 


Generated Columns :
-----to first generate a column no_days_taken_to_heal with respect to Bone Mass Density by the excel formula : =IF(F2>=-1,"42-56 days", IF(F2>-2.5,"56-84 days", "84-112+ days"))
-----later stages to generate column with number_of_days given in fracture haematoma (FxH), Soft callus formation, hard callus formation and remodelling
With other columns being self explanatory by name and having only reported values, for research basis focusing on calculated column STD

For diverse data and boundary case testing I am considering 5 set of AI generate rows which have T score in such a way that it gives No of healing days required more.
These are - sr. 10,27,..etc

STD
	• The STD column in this dataset is a technical DXA scan parameter, not the statistical standard deviation of the dataset.
	• The machine’s STD values are useful for quality control of scans, ensuring the BMD/T-score readings are reliable.
	• STD often refers to the Scan Standard Deviation or Scan Precision Index.

<    Further research to study extent of fractures
Human Bone Fractures Multi-modal Image Dataset
https://data.mendeley.com/datasets/xwfs6xbk47/1     >

----Library to be used
import numpy as np
from collections import Counter
-----To populate fracture type="only one kind at a time", age, health condition, and treatment quality
-----For KNN Prediction 
-----To consider BMD and an AI populated column(Number of days taken to heal by the individual) with limited available data

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




If your goal is to study fracture healing progression, you’ll likely need to:
	Combine fracture detection datasets (like Mendeley’s X-ray dataset) with clinical notes or EHR datasets.
	Look into orthopaedic clinical trials for longitudinal healing data.
  Collaborate with hospitals or research institutions under data-sharing agreements, since healing records are rarely open-access.
