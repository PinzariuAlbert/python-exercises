# EX 1 2 and 3
class Elevator:
    def __init__(self,bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor=self.bottom_floor
    def go_to_floor(self,floor_number):
        while(self.current_floor!=floor_number):
            if self.current_floor<floor_number:
                self.floor_up()
            else: self.floor_down()
            print(f"Current floor: {self.current_floor}")
        
    def floor_up(self):
        self.current_floor+=1
    def floor_down(self):
         self.current_floor-=1

class Building(Elevator):
    def __init__(self, bottom, top, total_elev):
        self.elevator_list = []
        self.total_elev = total_elev
        for n in range(total_elev):
             self.elevator_list.append(Elevator(bottom[n],top[n]))
    def run_elevator(self,elevator_number,floor_number):
        print(f"Running elevator number: {elevator_number}")
        self.elevator_list[elevator_number-1].go_to_floor(floor_number)
    def fire_alarm(self):
        for n in range(self.total_elev):
            print(f"Current elevator that's goint down: {n+1}")
            self.elevator_list[n].go_to_floor(0)
building = Building([0,0,0],[12,10,8],3)
building.run_elevator(1,5)
building.run_elevator(2,8)
building.run_elevator(3,3)

building.fire_alarm()

#4
import random

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
class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.name = kilometers
        self.car_list = car_list