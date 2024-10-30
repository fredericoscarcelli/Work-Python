class Point():
    def __init__(self, input1, input2):  # constructor
        self.x = input1
        self.y = input2


p = Point(3, 8)

# print(p.x)
# print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_Passanger(self, name):
        if not self.open_Seats():
            print("Flight is full")
            return False
        else:
            self.passangers.append(name)
            print(self.passangers)
            return True

    def open_Seats(self):
        return self.capacity - len(self.passangers)


flight = Flight(3)
people = ["Fred", "Cinthia", "Fabi", "Ceci"]

for person in people:
    success = flight.add_Passanger(person)
    if success:
        print(f"Added {person} to flight sucessfully")
    else:
        print(f"No available seats for {person}")
