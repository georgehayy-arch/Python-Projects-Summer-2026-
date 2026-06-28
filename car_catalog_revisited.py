from pathlib import Path
import statistics

# Creating the car class
class Car: 
    def __init__(self,make,model,year):

        self.make = make.title()
        self.model = model.title()
        self.year = int(year)

    # relaying user friendly message to user.
    def __str__(self):

        return f"{self.year} {self.make}{self.model}"

    # relaying debugging message
    def __repr__(self):
        
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

# Loading Car objects from CSV file

def load_cars(filename="cars.csv"):
    """ Read the CSV file and create Car objects """

    cars = []

    path = Path(filename)

    with path.open("r") as file: 
        next(file)

        for line in file:
            make, model, year = line.strip().split(",")
            car = Car(make, model, year)
            cars.append(car)
    return cars


# Finding cars by make from the CSV file
def get_cars_by_make(cars,make=""):
    """Return every car matching the given make
    """

    if make == "":
        make = input("Enter a car make: ")

    matching = []

    for car in cars:
        if car.make.lower() == make.lower():
            matching.append(car)

    return matching


# Creating a user interface to verify class development

if __name__ == "__main__":

    # Creating 3 samole objects
    car1 = Car("Toyota", "Camry", 2019)
    car2 = Car("Honda", "Civic", 2021)
    car3 = Car("Ford", "Mustang", 1968)

    print("Using ___str___()")
    print(car1)
    print(car2)
    print(car3)


    print("\nUsing __repr___()")
    print(repr(car1))
    print(repr(car2))
    print(repr(car3))

    cars = load_cars()

    



        

