import pandas as pd


# Creating a sample dataset for a fitness tracking application
data = {
    "User": ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley"],
    "Workout_type": ["Cardio", "Lifting", "Yoga", "Cardio", "Lifting", "Yoga"],
    "Calories_burned": [320, 450, 180, 290, 500, 210],
    "Minutes_spent": [30, 45, 60, 25, 50, 40]
}

# Converting our dictionary into a pandas DataFrame (pandas table)
df = pd.DataFrame(data)
print("\n--- Fitness Dataset ---")
print(df)

# Example #1: using the groupby() method
# Grouping the data by category and calculating the total values for each. 

calorie_summary = df.groupby("User")["Calories_burned"].sum() 
print("\n--- Total Calories Burned Per User ---")
print(calorie_summary)

# Example #2: using the describe() method
# Getting a statistical summary of the dataset. (Averages, min, max, etc.)

statistics_summary = df["Calories_burned"].describe()
print("\n--- Statistical Summary of Calories Burned ---")
print(statistics_summary)

# Example #3: Boolean Masking (Filtering)
# Filtering the dataset based on some condition. In this case, we are filtering for users who burned more than 300 calories.
high_performers = df[df["Calories_burned"] > 300]
print("\n--- Users Who Burned More Than 300 Calories ---")
print(high_performers)

# Looping through the filtered dataset to clean up the data and display it in a more readable format.
print("\n--- High Performers (FORMATTED) ---")
for index, row in high_performers.iterrows():
    print(f"{row['User']} burned {row['Calories_burned']} calories in {row['Minutes_spent']} minutes during their {row['Workout_type']} workout.")