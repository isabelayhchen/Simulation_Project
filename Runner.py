from Boarding_Line import Boarding_Line
from Passenger import Passenger
from World import Time, Space
import numpy as np
import random

# creating passengers
location = [0, 0]
passengers = []
for i in range (10):
    assigned_seat = [int(np.random.rand()*100), 0]
    print(assigned_seat)
    passengers.append(Passenger(assigned_seat, location, Space()))
def simulate(line, time, whileboarding = False):
    t = 0
    if whileboarding == False:
        for t in range(time):
            print("\n")
            print(len(line.line), "\n") #want to create space between the timesteps
            print("FOR TIME STEP: t = " + str(t) + " to " + str(t + 1) + "\n")
    elif whileboarding == True:
        while (len(line.line) > 0) and (t < 100): #while some passengers aren't seated
            t = t + 1
            print("FOR TIME STEP: t = " + str(t) + " to " + str(t + 1) + "\n")
            print("\n")
            print(len(line.line))
            line.update_line([1, 0])

# creating a Boarding line
passenger_list = [i for i in range(9)]
random.shuffle(passenger_list)
passenger_list_1 = [passengers[index] for index in passenger_list]
passenger_list_2 = [passengers[index] for index in passenger_list]

print("__________________SIMULATION 1______________________")
simulate(Boarding_Line(passenger_list_1), 10)
print("__________________SIMULATION 2______________________")
simulate(Boarding_Line(passenger_list_2), 10, True)
