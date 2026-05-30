import math
import datetime

#Assumptions used for every order
slices_per_pizza = 8
slices_per_person = 3
pizza_cost = 12.50

# Obtaining user info for order
name = input("What is the name that should be on the order?")
party_size = int(input("How many people will be at the party?"))

# Informing the user of the assumptions
print(f"The following assumptions are being made:")
print(f"- Each pizza has {slices_per_pizza} slices")
print(f"- Each person will eat {slices_per_person} slices")
print(f"- Each pizza costs ${pizza_cost:.2f}")

#Calculations needed for order total
total_slices_needed = party_size * slices_per_person
total_pizzas_needed = math.ceil(total_slices_needed / slices_per_pizza)
total_cost = total_pizzas_needed * pizza_cost

#User - friendly message relaying information about the order
name = name.capitalize()

print(f"Hello, {name}!")
print(f"Order date: {datetime.date.today()}")
print(f"Total slices needed: {total_slices_needed}")
print(f"Total pizzas needed: {total_pizzas_needed}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Fun fact, {name}, did you know that you have ")
print(f"{len(name)} letters in your name?")