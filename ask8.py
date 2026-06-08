import random

# Asking the user for their name.
user_name = input("What is your name?\n> ")

# Entering "Guest" if the user does not provide a name.
if not user_name: "Guest"

# Formatting the name to be title case.
user_name = user_name.title() 

# Greeting the user.
print(f"Welcome, {user_name}!") 

# Message displayed based on the length of the user's name.
if len(user_name) < 4:
    print("\nYour name is short and sweet!")
elif len(user_name) <= 6:
    print(f"\nGreat name! Balanced and bold.")
else:
    print(f"\nYour name carries power in every letter!")

    # Ask the user for their yes or no question.
    question = input("f\nPlease enter your yes or no question  {user_name}\n>")

    # Generate a random number for the response.
    answer_number = random.randint(1, 5) 

    # Display the response heading.
    print("\nThe Magic 8-Ball says:") 

    # Choose and display the response based on the random number.
    if answer_number == 1:
        print(f"\nYes, definetly.\n")
    elif answer_number == 2:
        print(f"\nNo, certainly not.\n")
    elif answer_number == 3:
        print(f"\nAsk again later.\n")
    elif answer_number == 4:
        print(f"\nOutlook not so good.\n")
    else: 
        print(f"\nIt is possible\n")