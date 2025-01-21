import pandas as pd
data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Married", "Single", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "Yes", "Yes", "No", "Yes", "No", "No", "Yes"]
}

df = pd.DataFrame(data)

print("Dataset:\n",df)

rows=df.loc[[0,4,7,8]]
print(rows)
r1=df.loc[3:7]
print(r1)
r2=df.loc[4:8,["Marital Status","Taxable Income","Cheat"]]
print(r2)
r3=df.iloc[:,1:4]
print(r3)
