#



class Parant():
    def vehicle(self,car,bike):
        self.car=car
        self.bike=bike


    def display(self):
        print(f"i have a {self.car} car and {self.bike} bike")


class Child(Parant):
    pass



obj1=Child()
obj1.vehicle(car="Mini chooper",bike="Himalaya")
obj1.display()