# Fracture-healing-using-knn
To take clinical data, consider Bone mass density and predict healing of a fracture based on the variables
Take BMD of patient and calculate the standard deviation from the other previously healed individual patient having similar or near about BMD in their case using K nearest neighbour algorithm.

Dependencies -
	1. Available open source dataset online.
	2. Different patients' individual body vitals.
	3. Extent and volume of data.

Objective - 
	1. To determine the healing days required to keep the plaster on and other supportive aids for the patient.
	2. To confirm palpation tests.

Definitions -

-----types of tests done by doctors before plaster is opened - visual inspection, palpation, circulation test, neurological checks, movement and function.
-----Columns in Dataset available
Sr. No |	Gender	| Age	| Height |	Weight |	BMD |	T_Score |	Z_Score |	Area |	BMC |	BMI |	Obesity | Group	| BFP	| STD

From <https://data.mendeley.com/datasets/kys6x6wykj/1/files/de8d831f-472e-409e-8bf4-4495fdc309d7> 

-----to generate column with number_of_days given in fracture haematoma (FxH), Soft callus formation, hard callus formation and remodelling
With other columns being self explanatory by name and having only reported values, for research basis focusing on calculated column STD

STD
	• The STD column in this dataset is a technical DXA scan parameter, not the statistical standard deviation of the dataset.
	• The machine’s STD values are useful for quality control of scans, ensuring the BMD/T-score readings are reliable.
	• STD often refers to the Scan Standard Deviation or Scan Precision Index.

<    Further research to study extent of fractures
Human Bone Fractures Multi-modal Image Dataset
https://data.mendeley.com/datasets/xwfs6xbk47/1     >

If your goal is to study fracture healing progression, you’ll likely need to:
	Combine fracture detection datasets (like Mendeley’s X-ray dataset) with clinical notes or EHR datasets.
	Look into orthopaedic clinical trials for longitudinal healing data.
  Collaborate with hospitals or research institutions under data-sharing agreements, since healing records are rarely open-access.
