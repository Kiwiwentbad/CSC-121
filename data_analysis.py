# Nikiya Woodard

import pandas as pd
import matplotlib.pyplot as plt

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
print()
print(largest_year_count)

# Display smallest year count
#print(year_count.min())



# Plot comic name and active year

plt.plot(df['comic_name'], df['active_years'])
plt.xlabel("Comic name")
plt.ylabel("active_year")
plt.title("Comic name with the active years")
plt.savefig("output.pnt")
plt.show()