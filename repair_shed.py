class SparePart():
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

class Car():
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.spare_parts = []

class Customer():
    def __init__(self, name, address, number, car):
        self.name = name
        self.address = address
        self.number = number
        self.car = car

        self.worker = None
        self.history_of_workers = []

    #смена машины
    def change_car(self, car):
        self.car = car
        print(self.name + " сменил машину")
        print("Марка машины: " + self.car.manufacturer)
        print("Модель: " + self.car.model)
        print("Год выпуска: " + self.car.year)
        print()

class Worker():
    def __init__(self, name):
        self.name = name

        self.wage = None
        self.earnings = 0
        self.customer = None
    #добавление запасной части
    def add_spare_part(self, part):
        self.customer.car.spare_parts.append(part)
        print("Добавлена новая запчасть машине клиента " + self.customer.name)
        print("Cтоимость за единицу: " + str(part.cost) + " денег")
        print("Количество: " + str(part.quantity))
        print()

class Manager():
    def __init__(self):
        self.__list_of_workers = []
        self.__history_of_customers = []
        self.__income = 0
    #добавление нового работника
    def add_worker(self, worker, wage):
        worker.wage = wage
        self.__list_of_workers.append(worker)
        print("Поступил работник " + worker.name)
        print()
    #добавление необязательно нового клиента, просто регистрация визита
    def add_customer(self, customer, worker):
        self.__history_of_customers.append(customer)
        print("Поступил клиент " +
              customer.name)
        print("тлф. " + customer.number + " адрес: " + customer.address)
        print("Марка машины: " + customer.car.manufacturer)
        print("Модель: " + customer.car.model)
        print("Год выпуска: " + customer.car.year)
        print()
        customer.worker = worker
        customer.history_of_workers.append(worker)
        worker.customer = customer
        print("С клиентом " +
              customer.name +
              " работает " +
              worker.name)
        print()
    #получение стоимости всех запасных частей для машины клиента
    def get_cost_of_parts(self, customer):
        return sum(list(map(lambda x: x.cost*x.quantity, customer.car.spare_parts)))
    #получение стоимости работы сотрудника с машиной клиента
    def get_cost_of_service(self, customer):
        return customer.worker.wage
    #получение общей стоимости работ с машиной клиента
    def get_total_cost(self, customer):
        return self.get_cost_of_parts(customer)+self.get_cost_of_service(customer)
    #проведение оплаты (работнику сразу начисляется зп)
    def payment(self, customer):
        self.__income += self.get_total_cost(customer)
        print("Клиент " +
              customer.name +
              " оплатил ремонт в размере " +
              str(self.get_total_cost(customer)) +
              " денег")
        customer.car.spare_parts = []

        customer.worker.earnings += self.get_cost_of_service(customer)
        print("Работнику " +
              customer.worker.name +
              " начислено " +
              str(self.get_cost_of_service(customer)) +
              " денег")
        print()

    def show_customer_history(self, customer):
        print("Список сотрудников, работавших с клиентом:")
        print(list(map(lambda x: x.name, customer.history_of_workers)))
        print()

    def show_worker_earnings(self, worker):
        print("На данный момент работник " +
              worker.name + " заработал " +
              str(worker.earnings) + " денег")
        print()

    def show_income(self):
        print("Всего наша замечательная компания на данный момент заработала " +
              str(self.__income) +
              " денег")
        print()

    def show_list_of_workers(self):
        print("У нас работают:")
        print(list(map(lambda x: x.name, self.__list_of_workers)))
        print()

    def show_history_of_customers(self):
        print("История посещений клиентов:")
        print(list(map(lambda x: x.name, self.__history_of_customers)))
        print()

    def show_payroll(self):
        print("Зарплатная ведомость:")
        print({person.name: person.earnings for person in self.__list_of_workers})
        print()

markV = Car("Старк Индастриз", "Марк V", "2013")
stark = Customer("Тони Старк", "Большая башня с буквой А", "8 (800) 555 35 35", markV)
happy = Manager()
peter = Worker("Питер")
happy.add_worker(peter, 100)
happy.add_customer(stark, peter)
engine = SparePart("Портативный реактор", 3000, 2)
peter.add_spare_part(engine)
happy.payment(stark)
happy.show_customer_history(stark)
happy.show_worker_earnings(peter)

markVI = Car("Старк Индастриз", "Марк VI", "2013")
stark.change_car(markVI)
happy.add_customer(stark, peter)
helmet = SparePart("Шлем", 1500, 1)
peter.add_spare_part(helmet)
happy.payment(stark)
happy.show_customer_history(stark)
happy.show_worker_earnings(peter)

pepper = Worker("Пеппер")
happy.add_worker(pepper, 200)
markI = Car("Старк Индастриз", "Марк I", "2008")
stark.change_car(markI)
happy.add_customer(stark, pepper)
chestplate = SparePart("Грудной корпус", 1000, 1)
peter.add_spare_part(chestplate)
happy.payment(stark)
happy.show_customer_history(stark)
happy.show_worker_earnings(pepper)

happy.show_income()
happy.show_list_of_workers()
happy.show_history_of_customers()
happy.show_payroll()
