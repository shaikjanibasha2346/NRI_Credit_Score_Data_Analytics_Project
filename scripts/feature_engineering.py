import pandas as pd

# Sample NRI data
data = {
    "monthly_income": [5000, 8000, 12000],
    "employment_years": [2, 4, 7],
    "remittance_amount": [1500, 2500, 4000]
}

df = pd.DataFrame(data)

# Credit score calculation
df["credit_score"] = (
    df["monthly_income"] * 0.3 +
    df["employment_years"] * 50 +
    df["remittance_amount"] * 0.2
)

print("Final Credit Score Output:")
print(df)
