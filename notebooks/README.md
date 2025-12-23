Task 1 – Data Analysis and Preprocessing
Objective

The objective of Task 1 is to prepare clean, feature-rich datasets for fraud detection modeling.
This task focuses on understanding the data, engineering meaningful features, integrating geolocation information, and addressing the critical challenge of class imbalance, which is common in fraud detection problems.

Task 1 ensures that the datasets are model-ready, interpretable, and aligned with real-world business constraints.

Datasets Used

1. Fraud_Data.csv (E-commerce Transactions)

User and transaction-level data

Target variable: class

1 → Fraudulent transaction

0 → Legitimate transaction

Highly imbalanced dataset

2. IpAddress_to_Country.csv

Maps IP address ranges to countries

Used to enrich fraud data with geolocation features

3. creditcard.csv (Bank Transactions)

PCA-transformed transaction features (V1–V28)

Target variable: Class

Extremely imbalanced dataset

Notebook Structure for Task 1

Task 1 is intentionally split across three notebooks for clarity and modularity:

notebooks/
├── eda-fraud-data.ipynb
├── feature-engineering.ipynb
├── eda-creditcard.ipynb

1. eda-fraud-data.ipynb
   Exploratory Data Analysis & Cleaning (Fraud_Data.csv)

This notebook covers:

Data cleaning

Handling missing values with justification

Removing duplicate records

Correcting data types (timestamps, numeric fields)

Exploratory Data Analysis (EDA)

Univariate analysis (distributions of key variables)

Bivariate analysis (relationship between features and fraud)

Class distribution analysis to quantify imbalance

Outcome:
A cleaned and well-understood e-commerce fraud dataset, with clear evidence of class imbalance.

2. feature-engineering.ipynb
   Geolocation Integration, Feature Engineering & Imbalance Handling

This notebook performs the core feature preparation steps for Fraud_Data.csv:

Geolocation Integration

Converted IP addresses to integer format

Merged fraud data with country data using range-based IP lookup

Analyzed fraud patterns by country

Feature Engineering

Time-based features:

hour_of_day

day_of_week

time_since_signup

Behavioral features:

Transaction frequency per user (transactions_per_user)

Data Transformation

Numerical features scaled using StandardScaler

Categorical features encoded using OneHotEncoder

Implemented preprocessing pipelines to prevent data leakage

Class Imbalance Handling

Applied SMOTE to the training data only

Documented class distribution before and after resampling

Justified SMOTE due to its ability to improve fraud recall without duplicating data

Outcome:
A fully transformed, balanced, and model-ready dataset for e-commerce fraud detection.

3. eda-creditcard.ipynb
   EDA & Class Imbalance Handling (creditcard.csv)

This notebook focuses on bank transaction fraud:

Class distribution analysis (extreme imbalance)

Train–test split with stratification

Comparison of imbalance handling strategies:

SMOTE

Class-weighted Logistic Regression

Evaluation using imbalance-appropriate metrics:

ROC-AUC

Precision–Recall AUC

Visualization of Precision–Recall curves

Outcome:
A validated approach for handling severe imbalance in banking fraud data, with clear performance comparisons.
