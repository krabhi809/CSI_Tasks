class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
        else:
            self.speed = 0

    def get_speed(self):
        return self.speed


# Main program
car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Honda", "Civic", 2021)

car1.accelerate(30)
car2.accelerate(40)

print(car1.make, car1.model, "is running at", car1.get_speed(), "km/h")
print(car2.make, car2.model, "is running at", car2.get_speed(), "km/h")

car1.brake(10)
car2.brake(20)

print(car1.make, car1.model, "is running at", car1.get_speed(), "km/h")
print(car2.make, car2.model, "is running at", car2.get_speed(), "km/h")
