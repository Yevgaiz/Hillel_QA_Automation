class Car:
    total_cars = 0

    def __init__(self, make, model, fuel_capacity):
        """Initialize a new Car instance.
            Args:
            make (str): The manufacturer of the car.
            model (str): The model of the car.
            fuel_capacity (float): The fuel capacity of the car in liters."""

        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        Car.total_cars += 1

    def drive(self, distance):
        """Simulate driving the car a certain distance, and reduces the fuel level based on car fuel efficiency.
        Args:
        distance (float): The distance to drive in kilometers."""

        fuel_needed = distance / 15
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f'Drove {distance} km. Remaining fuel: {self.fuel_level:.2f} liters.')
        else:
            print('Not enough fuel to drive the requested distance.')

    def refuel(self, amount):
        """Refuel the car by a certain amount of liters. Ensures that the fuel level doesn't exceed the fuel capacity.
        Args:
        amount (float): The amount of fuel to be added in litres"""

        if Car.is_valid_fuel_amount(amount):
            if amount + self.fuel_level <= self.fuel_capacity:
                self.fuel_level += amount
                print(f'Refueled {amount} liters. Current fuel level: {self.fuel_level:.2f} liters.')
            else:
                print('Cannot refuel beyond the fuel tank capacity.')
        else:
            print('Invalid amount of fuel for refueling.')

    @classmethod
    def get_total_cars(cls):
        """Get the total number of Cars."""

        return print(f"Total number of cars created: {cls.total_cars}")

    @staticmethod
    def is_valid_fuel_amount(amount):
        """Check if the given amount of fuel is a valid positive number.
        Args:
        amount (float): The amount of fuel to validate."""

        return amount >= 0


car1 = Car('Toyota', 'Corolla', 50)
car2 = Car('Honda', 'Civic', 45)
car3 = Car('Ford', 'Mustang', 60)

car1.refuel(20)
car1.drive(200)

car2.refuel(200)
car2.drive(100)

car3.refuel(60)
car3.drive(1900)

car2.refuel(-200)
car2.drive(100)

Car.get_total_cars()

Car.is_valid_fuel_amount(100)

print(f'Is 20 liters a valid fuel amount? {Car.is_valid_fuel_amount(20)}')
print(f'Is -5 liters a valid fuel amount? {Car.is_valid_fuel_amount(-5)}')