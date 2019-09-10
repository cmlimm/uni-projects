class SparePart():
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def total(self):
        return cost*quantity

class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.needed_parts = []

    def define_needed_parts(self, part):
        self.needed_parts.append(part)

    def get_cost_of_parts(self):
        return sum(list(map(lambda x: x.total, needed_parts)))

class Client():
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

    def client_car(self, car):
        self.car = car

class Manager():
    def
