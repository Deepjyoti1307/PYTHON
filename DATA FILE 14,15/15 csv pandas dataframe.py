#Use Panda dataframe to store the data from the file and print it in tabular format
import pandas as pd
df = pd.read_csv('data.csv')
print("\nData in tabular format:")
print(df)
print("\nDataFrame Info:")
print(df.info())