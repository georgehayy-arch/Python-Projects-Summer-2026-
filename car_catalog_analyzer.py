from pathlib import Path
import statistics

def load_cars(file_name="cars.csv"):
    """_summary_

    Args:
        file_name (str, optional): _description_. Defaults to "cars.csv".
    """
    # Create an empty list to store the car data
    cars = [] 

    # Open the file and read its contents
    file_path = Path.cwd() / file_name

    # Open the file for reading 
    with file_path.open("r") as file:
        # Read one line at a time
        for line in file:

            # Remove extra spaces and newline characters
            line = line.strip()

            # Unpack the values from the csv line
            make, model, year = line.split(",")

            # Create a dictionary to represent the car
            car = {
                "make": make.title(),
                "model": model.title(),
                "year": int(year)
            }

            # Add the dictiionary to our list of cars
            cars.append(car)

            return cars
        
       # using *args to unpack the values from the dictionary
        def print_car(*args):
            """ 
            Receives:
            make, model, year

            """
            make, model, year = args
            print(f"{make} {model} ({year})")

    def get_cars_by_make(cars, make="Volkswagen"):
        """
        Finds and prints all the cars that match the specified make.

        Args:
            cars : list of dictionaries representing the car data.
            make : car make to search for. Defaults to "Volkswagen".
        """
        # Create a list to store the matching cars
        matching_cars = []

        # Iterate through the list of cars
        for car in cars:
            if car["make"].lower == make.lower():
                matching_cars.append(car) 

        # Print the matching cars
        if len(matching_cars) == 0:
            print(f"No cars found for {make.title()}")
        else:
            for car in matching_cars:
                print_car(
                    car["make"],
                    car["model"],
                    car["year"]
                )

                return matching_cars

    # ask the user for a car make to search for        
    user_make = input("Enter a car make to search for: ")

    get_cars_by_make(cars, user_make)

    # Create a function to identify the make with the oldest year
    lambda car: car["year"]

    # Create a function to display the oldest car(s) in the list
    def show_oldest_cars(cars):
        """
        Finds and displays all cars that match the oldest year in the list.

        Args:
            cars : list of dictionaries representing the car data.
        """
        # Find the smallest year value
        oldest_year = min(cars, key=lambda car: car["year"])["year"]
        print(f"\nOldest year in the list: {oldest_year}\n")

        # Find and display all cars that match the oldest year
        for car in cars: 
            if car["year"] == oldest_year:
                print_car(
                    car["make"],
                    car["model"],
                    car["year"]
                )

    # Create a function to get the average year of the cars in the list
    def get_average_year(cars):
        """
        Calculates and returns the average year of the cars in the list.

        Args:
            cars : list of dictionaries representing the car data.
        """
        # Empty dataset to store the years
        years = []
        # Iterate through the list of cars and add the year to the dataset
        for car in cars: 
            years.append(cars["year"])

        # Calculate the average year using the statistics module
        average = statistics.mean(years)

        # Round to 0 decimal and convert to integer
        average = int(round(average, 0))

        # Return user friendly message
        return f"The average car year is {average}"
    
    # Sorting the cars by make via lambda
    def show_all_cars_sorted(cars):
        """
        Displays all cars sorted by make.

        Args:
            cars : list of dictionaries representing the car data.
        """
        # Sort alphabetically by make using the sorted function and a lambda function as the key
        sorted_cars = sorted(
            cars, key=lambda car: car["make"]
        )
        for car in sorted_cars:
            print_car(
                car["make"],
                car["model"],
                car["year"]
            )
    
    # Create a simple menu function for users that repeats until they choose to exit
    def show_menu():
        """
        Displays a menu of options for users
        """

        print("\nChoose a report:")
        print("1. View all cars sorted by make")
        print("2. Filters cars by make")
        print("3. Show the olderst car(s)")
        print("4. Show the average year of the cars")
        print("5. Exit")

    # Creating a loop to show the menu until the user chooses to exit
    def main():
        """
        Main program loop that shows the menu and processes user input.
        """

        # Load the cars from the file
        cars = load_cars()

        # Defailt menu choice
        choice = ""
        # Loop until the user chooses to exit
        while choice != "5":
            show_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                show_all_cars_sorted(cars)
            
            elif choice == "2":
                user_make = input("Enter a car make to search for: ")
                get_cars_by_make(cars, user_make)
            elif choice == "3":
                show_oldest_cars(cars)
            elif choice == "4":
                print(get_average_year(cars))
            elif choice == "5":
                print("Goodbye!")
            else:
                print("Invalid choice. Please try again.")            

