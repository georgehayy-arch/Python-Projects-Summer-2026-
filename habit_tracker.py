from datetime import date, timedelta

# Continue running program until user presses enter.
while continue_tracking == "y":
    # Ask the user for their name.
    name = input("Enter your name: ")

    # Ask the user to enter the starting date.
    year = int(input("Enter the starting year: "))
    month = int(input("Enter the starting month: "))
    day = int(input("Enter the starting day: "))

    # Create a date using the user's input.
    start_date = date(year, month, day)

    # Display the starting date.
    print(f"You entered as your starting date: {start_date}")

    # Ask how many days the habit will be tracked.
    total_days = int(input("How many days are you tracking? "))

    # Ask which habit the user hopes to track.
    habit = input(
        "What habit do you want to track?"
      "For example: study, exercise, etc. "
      )

    # Keeping track of successful days
    successful_days = 0

    # Loop through each day of the tracking period
    for day_number in range(1, total_days + 1):
        response = input(
            f"Did you {habit} on day {day_number}?"
            "Please Answer 'yes' or 'no': "
        )

        # Increase counter if the user successfully completed the habit.
        if response.lower() == "yes":
            successful_days += 1
        
    # Calculate the ending date of the tracking period.
    end_date = start_date + timedelta(days=total_days)

    # Calculate the success rate
    success_rate = (successful_days / total_days) * 100

    # Calculate how many days ago the tracking period ended.
    today = date.today()
    days_ago = (today - end_date).days

    # Creating/Displaying a summary.
    print("------Summary------")
    print(f"Habit tracker for {name.capitalize()}:")
    print(f"Habit: {habit.upper()}")
    print(
        f"Tracking period: "
        f"{start_date.strftime('%B %d, %Y')}"
        f"to {end_date.strftime('%B %d, %Y')}"
    )
    print(f"Completed {successful_days} out of {total_days} days.")
    print(f"Success rate: {success_rate:2f}%")
    print(f"Your tracking period ended {days_ago} days ago")

    # Ask the user if they would like continue.
    continue_tracking = input(
        "Would you like to track something else?"
        "Hit 'y' to continue, or press 'Enter' to quit: "
    )
    

    