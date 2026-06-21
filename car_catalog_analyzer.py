from pathlib import Path
import statistics

def load_cars(file_name="cars.csv"):
    """Load car data from a CSV file."""
    cars = []
    file_path = Path.cwd() / file_name

    with file_path.open("r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            make, model, year = line.split(",")
            car = {
                "make": make.title(),
                "model": model.title(),
                "year": int(year)
            }
            cars.append(car)

    return cars


def print_car(make, model, year):
    """Print a single car entry."""
    print(f"{make} {model} ({year})")


def get_cars_by_make(cars, make="Volkswagen"):
    """Find and print all cars that match the specified make."""
    matching_cars = []

    for car in cars:
        if car["make"].lower() == make.lower():
            matching_cars.append(car)

    if len(matching_cars) == 0:
        print(f"No cars found for {make.title()}")
    else:
        for car in matching_cars:
            print_car(car["make"], car["model"], car["year"])

    return matching_cars


def show_oldest_cars(cars):
    """Find and display all cars that match the oldest year in the list."""
    oldest_year = min(cars, key=lambda car: car["year"])["year"]
    print(f"\nOldest year in the list: {oldest_year}\n")

    for car in cars:
        if car["year"] == oldest_year:
            print_car(car["make"], car["model"], car["year"])


def get_average_year(cars):
    """Calculate and return the average year of the cars in the list."""
    years = [car["year"] for car in cars]
    average = int(round(statistics.mean(years), 0))
    return f"The average car year is {average}"


def show_all_cars_sorted(cars):
    """Display all cars sorted by make."""
    sorted_cars = sorted(cars, key=lambda car: car["make"])
    for car in sorted_cars:
        print_car(car["make"], car["model"], car["year"])


def show_menu():
    """Display the user menu."""
    print("\nChoose a report:")
    print("1. View all cars sorted by make")
    print("2. Filters cars by make")
    print("3. Show the olderst car(s)")
    print("4. Show the average year of the cars")
    print("5. Exit")


def main():
    """Main program loop that shows the menu and processes user input."""
    cars = load_cars()
    choice = ""

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


if __name__ == "__main__":
    main()
