class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self.__enable_auto_run = is_enable

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
print(tesla_car.model)
print(tesla_car.enable_auto_run)
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)