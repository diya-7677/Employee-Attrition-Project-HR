import os
import numpy as np
import pandas as pd

df = pd.read_csv("hr_analytics_attrition_project.csv")

# Check for duplicates and remove them
print("Before:", df.shape)
df.drop_duplicates(inplace=True)
print("After:", df.shape)

# correct label mismatches
df["Department"] = df["Department"].replace({

    "Tech": "Technology",

    "Cust Support": "Customer Support"

})
print(df["Department"].value_counts())

print(df.isnull().sum())

#Fills monthly salary missing values with median salary of respective department
df["Monthly_Salary"] = df.groupby("Department")["Monthly_Salary"]\
                         .transform(lambda x: x.fillna(x.median()))

print(df.isnull().sum())
print(df["Monthly_Salary"].describe())

#fill Missing values in Manager_Rating with mode department-wise
df["Manager_Rating"] = df.groupby("Department")["Manager_Rating"]\
                         .transform(lambda x: x.fillna(x.mode()[0])) 
print(df.isnull().sum())
print(df["Manager_Rating"].mode())
print(df["Manager_Rating"].value_counts())

#fill Missing values in Job_Satisfaction with overall medidan rounding by 2
df["Job_Satisfaction"] = df["Job_Satisfaction"].fillna(df["Job_Satisfaction"].median())
print(df.isnull().sum())
print(df["Job_Satisfaction"].median())

df.to_csv("hr_attrition_cleaned.csv", index=False)
print("Data cleaning completed. Cleaned data saved to 'hr_attrition_cleaned.csv'.")