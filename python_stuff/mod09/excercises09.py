import random
#1
class Car:
    def __init__(self,reg_number,max_speed=0,cur_speed=0,distance=0):
        self.reg_number=reg_number
        self.max_speed = max_speed
        self.cur_speed= cur_speed
        self.distance=distance
    def accelerate(self,change_speed):
        self.cur_speed+=change_speed
        if(self.cur_speed>self.max_speed):
            self.cur_speed=self.max_speed
        elif self.cur_speed<0:
            self.cur_speed=0
        return
    def drive(self, hours):
        self.distance+=hours*self.cur_speed    
newCar= Car("ABC-123",142)
print(newCar.reg_number,newCar.max_speed, newCar.cur_speed, newCar.distance)

#2
newCar.accelerate(70)
print(newCar.cur_speed)
newCar.accelerate(30)
print(newCar.cur_speed)
newCar.accelerate(50)
print(newCar.cur_speed)
newCar.accelerate(-200)
print(newCar.cur_speed)

#3
newCar.cur_speed=60
newCar.drive(1.5)
print(newCar.distance)

#4
cars=[]
for i in range(10):
    cars.append(Car(f"ABC-{i}", random.randint(100,200),0,0))
won=False
while(won!=True):
    for i in range(10):
        cars[i].accelerate(random.randint(-10, 15))
        cars[i].drive(1)
        if(cars[i].distance>=10000): won=True
for i in range(10):
    print(f"Car Number {i+1}. travelled {cars[i].distance} kilometers.")
