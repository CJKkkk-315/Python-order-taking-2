import pandas as pd
df = pd.read_csv('ml_case_training_data.csv')
print(df)
total = df.isnull().sum().sort_values(ascending=False)
print(total)