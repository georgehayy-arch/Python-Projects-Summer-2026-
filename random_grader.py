import random
from pathlib import Path 

# Creating file paths
input_file = Path("names_list.txt")
output_file = Path("names_output.txt")

# Read names from the input file
with open(input_file, "r") as file:
    data = file.read()
    
# Convert the data into a list of names
names = data.split(",")

# Clean up the names by stripping whitespace and capitalizing them
clean_names = []
for name in names:
    clean_names.append(name.strip())

# Create a dictionary
grades_dict = {}

# Generate random grades for each name and store them in the dictionary
for name in clean_names:
    grade = random.randint(50, 100)
    grades_dict[name] = grade 

# Write the names and their corresponding grades to the output file
with open(output_file, "w") as file: 
    for name, grade in grades_dict.items():
        file.write(
            f"{name} received a grade of {grade}\n"
        )
# Find the highest grade and the corresponding name
top_grade = max(grades_dict.values())
top_students = set()
for name, grade in grades_dict.items():
    if grade == top_grade:
        top_students.add(name)

# Find the lowest grade and the corresponding name
bottom_grade = min(grades_dict.values())
bottom_students = set()
for name, grade in grades_dict.items():
    if grade == bottom_grade:
        bottom_students.add(name)

# Calculate the average grade
average_grade = (
    sum(grades_dict.values()) / len(grades_dict)
)

# Display the results to the user
for student in top_students:
    print(
        f"The student with the top grade of {top_grade} is {student}."
    )
for student in bottom_students:
    print(
        f"The student with the bottom grade of {bottom_grade} is {student}."
    )

print()

print(
    f"The average grade is {average_grade:.1f}."
)