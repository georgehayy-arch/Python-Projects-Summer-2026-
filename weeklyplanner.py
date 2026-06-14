# Tuple containing the days of the week
days_of_week = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)
# Get user input for tasks
task_input = input("Enter your tasks (Comma separated): ")
# Convert the input string into a list of tasks
tasks = task_input.split(",")
# Clean up the tasks by stripping whitespace and capitalizing them
clean_tasks = []
for task in tasks:
    clean_tasks.append(task.strip().title())
# Display the cleaned tasks to the user
print("\nYour Tasks:")
for task in clean_tasks:
    print(task)
# Store the weekly plan in a list
weekly_plan = []
# Assign tasks to each day of the week
for day in days_of_week:

    assigned_task = ""
    while True:
        chosen_task = input(
            f"\nWhich task will you do on {day}? "
        )

        chosen_task = chosen_task.strip().title()
        if chosen_task in clean_tasks:
            assigned_task = chosen_task
            break
        else:
            print(f'"{chosen_task}" is not a valid task.')
            backup_choice = input(
                "Press T to try again or F for 'Free day':"
            )
            if backup_choice.strip().upper() == "F":
                assigned_task = "Free day"
                break 

# Store the days and their assigned tasks as tuples
day_task = (day,assigned_task)

# Add tuple to list
weekly_plan.append(day_task)

# Display the weekly plan to the user
print("\nYour Weekly Plan:\n")

for day, task in weekly_plan:
    print(f"{day:<10} -> {task}")

# Check for duplicate tasks in the weekly plan
assigned_tasks = []
for day, task in weekly_plan:
    assigned_tasks.append(task)

    printed = []
    printed()

    for task in assigned_tasks:
        if assigned_tasks.count(task) > 1 and task not in printed:
            print(
                f'You scheduled "{task}" {assigned_tasks.count(task)} times.'
            )

            printed.append(task)
