from pathlib import Path
import statistics

# Creating the car class 
class Car: 
    """Represents one car from the CSV file
    """
    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = int(year)

    def __str__(self):
        """Returns a user friendly message to users
        """
        return f"{self.make} {self.model} ({self.year})"

    def __repr__(self):
        """Returns a 'programmer-friendly' message for debugging
        """
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

# Loading the cars from the CSV file to this program
def load_cars(filename="cars.csv"):
    """
    Reading the CSV file and returning a list of Car objects
    """
    
    cars = []
    path = Path(filename)
    with path.open("r") as file:
        next(file)
        for line in file:
            make, model, year = line.strip().split(",")
            car = Car(make, model, year)
            cars.append(car)

    return cars


# Creating a method to view all cars by make
def view_all_cars(cars):
    """
    Displaying every car from CSV file sorted by make.
    """
    print("\n---- All Cars ----")
    for car in sorted(cars, key=lambda car: car.make):
        print(car)

# Filter cars by make (via user input)
def get_cars_by_make(cars):
    """
    Display all cars of a specific make based on what user has input
    """
    make = input("Enter a make: ")
    found = False

    for car in cars:
        if car.make.lower() == make.lower():
            print(car)
            found = True

    if not found:
        print("No cars of that make found.")

# Displaying oldest cars
def show_oldest_car(cars):
    """
    Display a list of the oldest car or cars.
    """
    oldest_year = min(car.year for car in cars)

    print("\nOldest Car(s):")
    for car in cars:
        if car.year == oldest_year:
            print(car)

# Disply average year
def get_average_year(cars):
    """
    Calculates and returns the average car year (rounded to nearest whole number).
    """
    years = []
    for car in cars:
        years.append(car.year)

    return round(statistics.mean(years))


#  Main program
if __name__ == "__main__":
    #testing __str__()
    print("Testing __str__()")
    car1 = Car("Toyota", "Camry", 2019)
    car2 = Car("Honda", "Civic", 2021)
    car3 = Car("Ford", "Mustang", 1968)

    print(car1)
    print(car2)
    print(car3)

    # Testing __repr__()
    print("Testing __repr__()")
    print(repr(car1))
    print(repr(car2))
    print(repr(car3))
    
    cars = load_cars()

    # Creating/Displaying user - interface
    while True:
        print("\n----- Car Catalog -----")
        print("1. View all Cars")
        print("2. Filter Cars by Make")
        print("3. Display Oldest Car(s)")
        print("4. Display Average Year")
        print("5. Exit")

        user_choice = input("Please select an option: ")

        if user_choice == "1":
            view_all_cars(cars)
        elif user_choice == "2":
            get_cars_by_make(cars)
        elif user_choice == "3":
            show_oldest_car(cars)
        elif user_choice == "4":
            print(f"\nAverage Year: {get_average_year(cars)}")
        elif user_choice == "5":
            print("\nThank you and Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

    
        
