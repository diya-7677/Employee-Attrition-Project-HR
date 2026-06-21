import numpy as np
import pandas as pd
import random

np.random.seed(42)
random.seed(42)

N = 15000

departments = {
    
    "Technology": {
        "salary": 120000,
        "overtime": 15,
        "remote_days": 3,
        "attrition_base": 0.12
    },

    "Operations": {
        "salary": 80000,
        "overtime": 18,
        "remote_days": 1,
        "attrition_base": 0.15
    },

    "Retail Banking": {
        "salary": 90000,
        "overtime": 16,
        "remote_days": 1,
        "attrition_base": 0.14
    },

    "Investment Banking": {
        "salary": 200000,
        "overtime": 30,
        "remote_days": 0,
        "attrition_base": 0.18
    },

    "Risk Management": {
        "salary": 140000,
        "overtime": 12,
        "remote_days": 2,
        "attrition_base": 0.10
    },

    "Compliance": {
        "salary": 130000,
        "overtime": 10,
        "remote_days": 1,
        "attrition_base": 0.08
    },

    "Finance": {
        "salary": 125000,
        "overtime": 14,
        "remote_days": 1,
        "attrition_base": 0.09
    },

    "Human Resources": {
        "salary": 85000,
        "overtime": 8,
        "remote_days": 2,
        "attrition_base": 0.06
    },

    "Customer Support": {
        "salary": 60000,
        "overtime": 25,
        "remote_days": 0,
        "attrition_base": 0.28
    },

    "Cyber Security": {
        "salary": 150000,
        "overtime": 20,
        "remote_days": 2,
        "attrition_base": 0.12
    }
}

def clip(x, low, high):
    return max(low, min(x, high))

employee_ids = [f"EMP{i:05d}" for i in range(1, N+1)]

gender = np.random.choice(
    ["Male", "Female", "Other"],
    N,
    p=[0.48, 0.48, 0.04]
)

education = np.random.choice(
    ["Bachelor", "Master", "MBA", "PhD"],
    N,
    p=[0.45, 0.30, 0.20, 0.05]
)

marital = np.random.choice(
    ["Single", "Married"],
    N,
    p=[0.40, 0.60]
)

department = np.random.choice(
    list(departments.keys()),
    N
)

location = np.random.choice(
    ["Pune", "Ahmedabad", "Bangalore", "Mumbai", "Hyderabad", "Chennai", "Kolkata", "Delhi", "Jaipur", "Lucknow"],
    N
)

age = np.random.randint(22, 60, N)

years_at_company = np.random.randint(0, 20, N)

employment_type = np.random.choice(
    ["Full-Time", "Contract"],
    N,
    p=[0.90, 0.10]
)

monthly_salary = []
overtime_hours = []
remote_work_days = []
attrition_base = []
projects_assigned = []
team_size = []

for dept in department:

    config = departments[dept]

    monthly_salary.append(
        np.random.normal(config["salary"], 10000)
    )

    overtime_hours.append(
        np.random.normal(config["overtime"], 4)
    )

    remote_work_days.append(
        config["remote_days"]
    )

    attrition_base.append(
        config["attrition_base"]
    )

    projects_assigned.append(
        np.random.randint(2, 8)
    )

    team_size.append(
        np.random.randint(4, 15)
    )

years_in_current_role = []

for years in years_at_company:

    years_in_current_role.append(
        np.random.randint(0, years+1)
        if years > 0 else 0
    )

promotion_last_3yrs = np.random.choice(
    [0,1],
    N,
    p=[0.65,0.35]
)

training_hours = np.random.normal(40,12,N)
training_hours = np.clip(training_hours,5,80)

performance_rating = []

for train in training_hours:

    score = round(
        np.random.normal(3 + train/50, 0.7)
    )

    performance_rating.append(
        clip(score,1,5)
    )

salary_hike_percent = []

for perf in performance_rating:

    if perf == 5:
        hike = np.random.uniform(18,22)

    elif perf == 4:
        hike = np.random.uniform(12,18)

    elif perf == 3:
        hike = np.random.uniform(8,12)

    elif perf == 2:
        hike = np.random.uniform(4,8)

    else:
        hike = np.random.uniform(1,4)

    salary_hike_percent.append(hike)

bonus = []

for salary in monthly_salary:
    bonus.append(
        salary * np.random.uniform(0.08,0.20)
    )

stock_options = []

for years in years_at_company:

    if years > 10:
        stock_options.append(np.random.randint(100,500))

    elif years > 5:
        stock_options.append(np.random.randint(30,100))

    else:
        stock_options.append(np.random.randint(0,30))

benefits_score = np.random.randint(5,10,N)

manager_rating = np.random.randint(1,6,N)

work_life_balance = []

for ot in overtime_hours:

    score = round(
        5 - (ot/10) + np.random.normal(0,0.5)
    )

    work_life_balance.append(
        clip(score,1,5)
    )

commute_distance = np.random.randint(2,50,N)

certification_count = []

for train in training_hours:

    cert = round(
        np.random.normal(train/20,1)
    )

    certification_count.append(
        clip(cert,0,8)
    )


job_satisfaction = []

for i in range(N):

    # normalize salary roughly to score 1–10
    salary_score = monthly_salary[i] / 25000

    satisfaction = (
        0.30 * manager_rating[i]
        + 0.25 * work_life_balance[i]
        + 0.20 * salary_score
        + 0.15 * promotion_last_3yrs[i] * 5
        - 0.10 * (overtime_hours[i] / 10)
        + np.random.normal(0,0.5)
    )

    # scale to 1–10
    satisfaction = round(satisfaction * 1.5)

    job_satisfaction.append(
        clip(satisfaction,1,10)
    )

engagement_score = []

for sat in job_satisfaction:

    engagement = round(
        sat * 10 + np.random.normal(0,8)
    )

    engagement_score.append(
        clip(engagement,1,100)
    )

absenteeism_days = []

for sat in job_satisfaction:

    if sat <= 3:
        days = np.random.randint(10,25)

    elif sat <= 6:
        days = np.random.randint(5,15)

    else:
        days = np.random.randint(0,7)

    absenteeism_days.append(days)

attrition = []

risk_score = []

for i in range(N):

    score = 0

    # Overtime creates burnout
    if overtime_hours[i] > 22:
        score += 2

    # Low salary dissatisfaction
    if monthly_salary[i] < 70000:
        score += 2

    # No promotion frustration
    if promotion_last_3yrs[i] == 0:
        score += 1

    # Poor manager relationship
    if manager_rating[i] <= 2:
        score += 2

    # Low job satisfaction
    if job_satisfaction[i] <= 4:
        score += 2

    risk_score.append(score)

    # Final decision
    if score >= 6:
        attrition.append(1)

    else:
        attrition.append(0)

high_risk_employee = []

for score in risk_score:

    if score >= 5:
        high_risk_employee.append(1)

    else:
        high_risk_employee.append(0)
        
df = pd.DataFrame({

    "Employee_ID": employee_ids,
    "Age": age,
    "Gender": gender,
    "Education_Level": education,
    "Marital_Status": marital,
    "Department": department,
    "Location": location,

    "Years_at_Company": years_at_company,
    "Years_in_Current_Role": years_in_current_role,
    "Promotion_Last_3Yrs": promotion_last_3yrs,
    "Employment_Type": employment_type,
    "Training_Hours": training_hours,

    "Monthly_Salary": monthly_salary,
    "Salary_Hike_Percent": salary_hike_percent,
    "Bonus": bonus,
    "Stock_Options": stock_options,
    "Benefits_Score": benefits_score,

    "Performance_Rating": performance_rating,
    "Manager_Rating": manager_rating,
    "Projects_Assigned": projects_assigned,
    "Certification_Count": certification_count,

    "Overtime_Hours": overtime_hours,
    "Work_Life_Balance": work_life_balance,
    "Commute_Distance_KM": commute_distance,
    "Remote_Work_Days": remote_work_days,
    "Team_Size": team_size,

    "Job_Satisfaction": job_satisfaction,
    "Engagement_Score": engagement_score,
    "Absenteeism_Days": absenteeism_days,

    "Attrition": attrition,
    "High_Risk_Employee": high_risk_employee
})

# Introduce some missing values to simulate real-world data issues
df.loc[df.sample(frac=0.03).index, "Manager_Rating"] = np.nan
df.loc[df.sample(frac=0.02).index, "Job_Satisfaction"] = np.nan
df.loc[df.sample(frac=0.02).index, "Monthly_Salary"] = np.nan

# Add some duplicates to simulate real-world data issues
duplicates = df.sample(frac=0.01)
df = pd.concat([df, duplicates])

# Label mismatches to simulate real-world data issues
df.loc[df.sample(frac=0.01).index, "Department"] = "Tech"
df.loc[df.sample(frac=0.01).index, "Department"] = "Cust Support"

df.to_csv("hr_analytics_attrition_project.csv", index=False)


print(df.shape)
print(df["Attrition"].value_counts(normalize=True))
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Department"].value_counts())