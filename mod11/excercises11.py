import random
#1
class Publication:
    publication_number = 0
    def __init__(self,self_name):
        Publication.publication_number+=1
        self.self_name=self_name

    def print_information(self):
        print(f"Publication name: {self.self_name}")

class Book(Publication):
    def __init__(self,self_name,author,pages):
        self.book_pages=pages
        self.book_author = author
        super().__init__(self_name)

    def print_information(self):
        super().print_information()
        print(f"The author is {self.book_author} and nr pages {self.book_pages}")
        

class Magazine(Publication):
    def __init__(self,self_name,editor):
        self.magazine_editor=editor
        super().__init__(self_name)

    def print_information(self):
        super().print_information()
        print(f"The magazine's editor is {self.magazine_editor}")

publications = []
publications.append(Magazine("Donald Duck","Aki Hyyppä"))
publications.append(Book("COmpartment No.6","Rosa Liksom", 192))

for p in publications:
    p.print_information()

#2
#I added the class from "excercises09.py"
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
class ElectricCar(Car):
    def __init__(self,  reg_number,max_speed, electrical_capacity,cur_speed=0,distance=0):
        self.electrical_capacity=electrical_capacity
        super().__init__(reg_number,max_speed,cur_speed=0,distance=0)

class GasolineCar(Car):
    def __init__(self, reg_number,max_speed,gas_volume, cur_speed=0,distance=0):
        self.gas_volume=gas_volume
        super().__init__(reg_number,max_speed,cur_speed=0,distance=0)

cars=[]
cars.append(ElectricCar("ABC-15", 180, 52.5))
cars.append(GasolineCar("ACD-123",165,32.3))
for c in cars:
    c.accelerate(random.randint(-10, 15))
    c.drive(3)
for i in range(2):
    print(f"Car {i+1}'s kilometer counter: {cars[i].distance}")