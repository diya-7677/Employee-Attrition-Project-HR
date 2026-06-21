import os
import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("hr_attrition_cleaned.csv")

# Attriiton rate in dataset
attrition_rate = round(df['Attrition'].value_counts(normalize=True) * 100,2)
print(attrition_rate)

# Department wise attrition rate
dept_attrition_rate = round(df.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100, 2)
print(dept_attrition_rate)

# Hypothesis 1: Compeneation and rewards analysis

# lower monthly salary might be a reason for higher attrition
monthly_salary_by_attrition = round(df.groupby("Attrition")["Monthly_Salary"].mean(), 2)
print(monthly_salary_by_attrition)

#lower salary hike might be a reason for higher attrition
salary_hike_by_attrition = round(df.groupby("Attrition")["Salary_Hike_Percent"].mean(), 2)
print(salary_hike_by_attrition)

#direct compensation might be a reason for higher attrition
bonus_by_attrition = round(df.groupby("Attrition")["Bonus"].mean(), 2)
print(bonus_by_attrition) 

#stock options might be a reason for higher attrition
stock_options_by_attrition = round(df.groupby("Attrition")["Stock_Options"].mean(), 2)
print(stock_options_by_attrition)   


# Hypothesis 2: Career growth and development opportunities
promotion_attrition_crosstab = round(pd.crosstab(
    df["Promotion_Last_3Yrs"],
    df["Attrition"],
    normalize="index"
) * 100, 2)
print(promotion_attrition_crosstab)

# years in current role might be a reason for higher attrition
years_in_current_role_by_attrition = round(df.groupby("Attrition")["Years_in_Current_Role"].mean(), 2)
print(years_in_current_role_by_attrition)

#training hours might be a reason for higher attrition
training_hours_by_attrition = round(df.groupby("Attrition")["Training_Hours"].mean(), 2)
print(training_hours_by_attrition)

#employment type might be a reason for higher attrition
employment_type_attrition_crosstab = round( pd.crosstab(
    df["Employment_Type"],
    df["Attrition"],
    normalize="index"
) * 100, 2)
print(employment_type_attrition_crosstab)   

# Hypothesis 3: Work environment 

#overtime might be a reason for higher attrition
overtime_attrition= round(df.groupby("Attrition")["Overtime_Hours"].mean(), 2)
print(overtime_attrition)     

#work life balance might be a reason for higher attrition
work_life_balance_by_attrition = round(df.groupby("Attrition")["Work_Life_Balance"].mean(), 2)
print(work_life_balance_by_attrition)

#remote work might be a reason for higher attrition 
remote_work_by_attrition = round(df.groupby("Attrition")["Remote_Work_Days"].mean(), 2)
print(remote_work_by_attrition)

# Hypothesis 4: Job satisfaction and engagement 

#job satisfaction might be a reason for higher attrition
job_satisfaction_by_attrition = round(df.groupby("Attrition")["Job_Satisfaction"].mean(), 2)
print(job_satisfaction_by_attrition)    

# engagement score might be a reason for higher attrition
engagement_score_by_attrition = round(df.groupby("Attrition")["Engagement_Score"].mean(), 2)
print(engagement_score_by_attrition)

# absenteeism days might be a reason for higher attrition
absenteeism_by_attrition = round(df.groupby("Attrition")["Absenteeism_Days"].mean(), 2)
print(absenteeism_by_attrition)

# Hypothesis 5: Performance and recognition

#performance rating might be a reason for higher attrition
performance_rating_by_attrition = round(df.groupby("Attrition")["Performance_Rating"].mean(), 2)
print(performance_rating_by_attrition)  

#maganer rating might be a reason for higher attrition
manager_rating_by_attrition = round(df.groupby("Attrition")["Manager_Rating"].mean(), 2)
print(manager_rating_by_attrition)  

#projects assigned might be a reason for higher attrition
projects_by_attrition = round(df.groupby("Attrition")["Projects_Assigned"].mean(), 2)
print(projects_by_attrition)

# High risk employees based on multiple factors
high_risk_attrition = pd.crosstab(
    df["High_Risk_Employee"],
    df["Attrition"],
    normalize="index"
) * 100
print(high_risk_attrition)