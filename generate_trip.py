import math
import numpy as np
import csv
import pandas as pd
import "class def.py" as cd

def rand_time_gen():
    mu, sigma = 12, 3
    start_time = np.random.normal(mu, sigma)
    return start_time

def journey_duration(distance):
    speed = (120*1000)
    duration = distance/speed     #in hour
    return duration

def end_time(duration):
    seconds = (duration + rand_time_gen())*60*60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d"%(hours,minutes,seconds)

def conv_time(time):
    seconds = (duration + rand_time_gen())*60*60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%02d:%02d:%02d"%(hours,minutes,seconds)

with open('airtrip.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Start Time', 'End Time','Duration',
                        'Departure','Depart Latitude','Depart Longitude',
                        'Destination', 'Dest Latitude', 'Dest Longitude'])

df = pd.read_csv('airtrip.csv')
