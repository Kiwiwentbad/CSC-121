# Nikiya Woodard

import pandas as pd

# Read the csv file into a variable
df = pd.read_csv("Marvel_Comics.csv")

# Display first few rows in the dataset
print(df.head())

# Put active_years into a variable
year_count = df["active_years"]

# Display largest year count
#print(year_count.max())

largest_year_count = df[df['active_years'] == df['active_years'].max()]
print("Largest year of comic books collected")

# Display smallest year count
#print(year_count.min())