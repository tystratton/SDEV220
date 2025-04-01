class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

type = input("What type of vehicle do you want? ")
year = input(f"What year {type} do you want? ")
make = input(f"What make {type} do you want? ")
model = input(f"What model {type} do you want? ")
doors = input("How many doors do you want? ")
roof = input("What type of roof do you want? \n")

choice = Automobile(type, year, make, model, doors, roof)
print(f"Vehicle type: {choice.type}")
print(f"Year: {choice.year}")
print(f"Make: {choice.make}")
print(f"Model: {choice.model}")
print(f"Doors: {choice.doors}")
print(f"Roof: {choice.roof}")

