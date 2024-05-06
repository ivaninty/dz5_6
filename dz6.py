class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def write(self):
        print(f"Вік = {self.age}\n"
              f"Ім'я = {self.name}\n")


class Driver_bus(Person):
    def __init__(self,name,age,driver_license_number):
        super().__init__(name,age,)
        self.driver_license_number = driver_license_number

    def write(self):
        super().write()
        print(f"Номер водійського посвідчення = {self.driver_license_number}")
class Driver_car(Person):
    def __init__(self,name,age,driver_license_number):
        super().__init__(name,age,)
        self.driver_license_number = driver_license_number

    def write(self):
        super().write()
        print(f"Номер водійського посвідчення = {self.driver_license_number}")

person_1 = Driver_car("Matviy",32,3343231)
person_2 = Driver_bus("Ivan",19,4846284)

person_1.write()
person_2.write()