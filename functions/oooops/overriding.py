class Parant():
    def vehicle(self,car,bike):
        self.car=car
        self.bike=bike


    def display_car(self):
        print(f"i have a {self.car}")
    
    def display_bike(self):
        print(f"i have a {self.bike}")



class Child(Parant):
    def display_car(self):
        print(f" I have a GTR")



obj1=Child()
obj1.vehicle(car="Mini chooper",bike="Himalaya")
obj1.display_car()
obj1.display_bike()