import time
from random import randint


def log(function):
    def wrapper(*args):
        file=open("machine.log",'a')
        start=time.time()
        file.write('(cmaxime)Running: {name}	[ exec-time = {time} ms ]\n'.format(name=function.__name__,time=start))
        file.close()
        return function(*args)
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        print("Please add water !")
        return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for i in range(20):
                time.sleep(0.1)
                CoffeeMachine.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self,water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    
    machine.make_coffee()
    machine.add_water(70)