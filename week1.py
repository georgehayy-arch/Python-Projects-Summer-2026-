import datetime

#asking the user for their name and age
user.name = input("What is your name?")
print(f"Hello, {user.name}!")
print(f"Today's date is {datetime.date.today()}")
age = int(input("How old are you?"))
print(f"Wow, in 10 years you will be {age + 10} years old!") #user friendly message using the age they provided