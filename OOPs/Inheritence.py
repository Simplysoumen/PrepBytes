class Car:
    def __init__(self, gears, seats, maxSpeed):
        self.gears = gears
        self.seats = seats
        self.maxSpeed = maxSpeed

    def speedup(self):
        print("Speed Increased")

    def apply_brake(self):
        print("Speed decreased")

    def movement(self):
        print("Car moves back and forth")

class Hyundai:
    def __init__(self):
        self.brandname = "Hyundai"

#Inheritence
class Skoda(Car):
    def racemode(self):
        print("Drifting")

    def __init__(self, milage, gears, seats, maxSpeed):
        self.milage = milage
        #Super method
        super().__init__(gears, seats, maxSpeed)

#Multiple Inheritence
class Verna(Car,Hyundai):
    def __init__(self, gears, seats, maxSpeed):
        Car.__init__(self, gears, seats, maxSpeed)
        Hyundai .__init__(self)

class PAL_V(Car):
    def movement(self):
        print("Car moves back, forth, up and down")

    c1= Car(4,12,129)
s1= Skoda(15, 5, 4, 240)
v1= Verna(5, 4, 180)
p1= PAL_V(5, 2, 300)
print(s1.milage)
print(s1.gears)
print(s1.seats)
print(s1.maxSpeed)
s1.speedup()
s1.apply_brake()
s1.racemode()
s1.movement()
print(v1.brandname)
print(v1.gears)
