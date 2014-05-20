#!/usr/bin/env python

import sys

try:
    time =int(sys.argv[1])
    track = int(sys.argv[2])
except:
    print 'didn\'t input value for time or track size'
    print 'ex. ./vehicledistance.py 120 30'
    sys.exit(-1)

class vehicle:
    def __init__(self,form,name,speed):
        self.name = name
        self.speed = speed
        self.form = form

    def calc_distance(self,time):
        return self.speed*time

if __name__=='__main__':
    horse = vehicle('horse','shetland',30)
    print horse.form, horse.name, 'distance traveled', horse.calc_distance(time)
    car = vehicle('car','lambourghini',120)
    print car.form, car.name, 'distance traveled', car.calc_distance(time)
    motorcycle = vehicle('motorcycle', 'harley', 60)
    print motorcycle.form, motorcycle.name, 'distance traveled', motorcycle.calc_distance(time)

    distance_v1 = horse.calc_distance(time)
    distance_v2 = car.calc_distance(time)
    difference = distance_v2 - distance_v1
    laps = difference / track

    if laps > 1:
        print 'v2 passed v1'
    else:
        print 'v2 did not pass v1'
