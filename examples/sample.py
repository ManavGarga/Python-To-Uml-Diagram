class Engine:
    def start(self):
        pass

class Driver:
    def drive(self):
        pass

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, driver):
        self.engine = Engine()     # composition (Car owns Engine)
        self.driver = driver       # aggregation (Car uses Driver)

    def start_car(self):
        self.engine.start()
        self.driver.drive()
