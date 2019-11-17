from random import uniform
from math import sin, cos, sqrt, atan2, radians
import time
import numpy as np
import math
import csv
import string

def random_location_pair_gen():
    current_lat = uniform(-0.309,0.181)
    current_long = uniform(51.423, 51.656)
    des_lat = uniform(-0.309,0.181)
    des_long = uniform(51.423, 51.656)
    return current_lat, current_long, des_lat, des_long

def distance():
    distance = 31
    while(distance > 30):
        L = random_location_pair_gen()
        R = 6373.0
        dlon = radians(L[3]) - radians(L[1])
        dlat = radians(L[2]) - radians(L[0])

        a = sin(dlat / 2)**2 + cos(radians(L[0])) * cos(radians(L[2])) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        if distance <= 30:
            return distance*1000, L #distance in m

def journey_duration():
    speed = (120*1000)
    duration = distance()/speed     #in hour
    return duration

def rand_time_gen():
    mu, sigma = 12, 3
    start_time = np.random.normal(mu, sigma)
    return start_time

def end_time():
    seconds = (journey_duration()+rand_time_gen())*60*60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d"%(hours,minutes,seconds)

F = distance()
print (F.split(",")[2])

#with open('mycsv.csv', 'w', newline='') as dat:
    #fieldnames = ['Start Time','End Time','Duration','Pick Up Latitude','Pick up Longitude','Drop Off Latitude','Drop Off Longitude']
    #data = csv.DictWriter(dat, fieldnames=fieldnames)

    #data.writeheader()
    #for i in range(1,1000):
    #    data.writerow({'Start time': rand_time_gen(),
    #    'End Time': (end_time()),
    #    'Duration':journey_duration(),
    #    'Pick Up Latitude': distance()[1],
    #    'Pick up Longitude': distance()[2],
    #    'Drop Off Latitude':distance()[3],
    #    'Drop Off Longitude':distance()[4] })
