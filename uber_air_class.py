import time


class taxi:
    def __init__(self, name):
        self.name = name
        self.speed = 33.3333
        self.battery = 900
        self.passenger = 0

    def pickup():
        self.passenger += 1
    def dropoff():
        self.passenger -= 1
    def direction(bound):
        if bound == 'W':
            self.level = westbound
        elif bound == 'E':
            self.level = eastbound
        elif bound == 'N':
            self.level = northbound
        elif bound == 'S':
            self.level = southbound
    #def charging():
        #self.battery
    #def flying():

bet365 = taxi("bet365")
booking = taxi("booking.com")
netcraft = taxi("netcraft")
arm = taxi("arm")
print(arm.name)
