class SparePart():
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
    # общая стоимость деталей данного вида
    def total(self):
        return cost*quantity

class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.needed_parts = []

    # добавление запчасти, необходимой для машины
    def add_needed_part(self, part):
        self.needed_parts.append(part)

    # получение общей стоимости запчастей для машины
    def get_cost_of_parts(self):
        return sum(list(map(lambda x: x.total, needed_parts)))

class Client():
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number
    # создание машины клиента (возможно, стоит метод перенести в класс Manager)
    def add_client_car(self, car):
        self.car = car

class Manager():
    pass
