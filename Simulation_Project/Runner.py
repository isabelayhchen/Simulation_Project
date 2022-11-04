from Boarding_Line import Boarding_Line
from Passenger import Passenger
from World import Time, Seats, Space, Compartment
import numpy as np
import random
import pandas as pd

import os, re, os.path

#global variables
seatcolumns = [1, 2, 6, 7]
aislecolumns = [4]
compartmentcolumns = [3, 5]
rows = 300 #for now the plane has 300 rows
totalcolumns = 7 #2 seats to the left + 2 seats to the right + 1 seat for an aisle + 2 columns for compartments = 7 columns
numpassengers = 100 #for now, 10 passengers
path = "/Users/etaashpatel/Downloads/Simulation_Project-main/outputs/"
#recording what happens at each time step
class book:
    def __init__(self, ):
        self.volume = [{}, {}, {}]
    def record(self, passengers, space, round): #recording what happened
        #record data as dataframes
        passengertable = pd.DataFrame([passenger.get_info() for passenger in passengers])
        passengertable.columns = ['Current Location', 'Assigned Seat', 'Passenger is Seated?', 'Passenger has Stowed Lugggage?', 'Passenger Walking Speed']
        compartments3 = {**space.opencompartments, **space.closedcompartments}
        compartmenttable = pd.DataFrame([[compartments3[compartment].location, compartments3[compartment].status] for compartment in compartments3.keys()])
        compartmenttable.columns = ['Compartment Location', 'Compartment Status']
        seats3 = {**space.openseats, **space.closedseats}
        seattable = pd.DataFrame([[seats3[seat].location, seats3[seat].status] for seat in seats3.keys()])
        seattable.columns = ['seat Location', 'seat Status']
        #write dataframes in the 'volume'
        self.volume[0]["round " + str(round)] = passengertable
        self.volume[1]["round " + str(round)] = compartmenttable
        self.volume[2]["round " + str(round)] = seattable
    def clear(self):
        self.volume = [{}, {}, {}]
    def write(self, directory = path, delete = False, passengername = 'passenger-actions', compartmentname = 'compartment-status', seatname = 'seat-status'):
        #delete all existing workbooks if delete = True
        if delete == True:
            for root, dirs, files in os.walk(path):
                for file in files:
                    os.remove(os.path.join(root, file))
        else:
            pass
        #add the new notebooks
        paths = [directory + passengername + '.xlsx', directory + compartmentname + '.xlsx', directory + seatname + '.xlsx']
        #add new sheets to those workbooks and transfer dataframes into them
        writer = pd.ExcelWriter(paths[0], engine = 'xlsxwriter') #for passengers
        for key in self.volume[0].keys(): 
            self.volume[0][key].to_excel(writer, sheet_name = key, index = False)
        writer.save()

        writer = pd.ExcelWriter(paths[1], engine = 'xlsxwriter') #for baggage compartments
        for key in self.volume[1].keys(): 
            self.volume[1][key].to_excel(writer, sheet_name = key, index = False)
        writer.save()

        writer = pd.ExcelWriter(paths[2], engine = 'xlsxwriter')#for seats
        for key in self.volume[2].keys(): 
            self.volume[2][key].to_excel(writer, sheet_name = key, index = False)
        writer.save()
        
history = book() #stores all relevant information

#the actual simulation
def generatespace(dimensions, layout, compartmentcapacity = 1):
    #unpacking inputs
    rows = dimensions[0]
    columns = dimensions[1]
    seat_columns = layout[0]
    compartment_columns = layout[1]
    aislecolumns = layout[2]
    #generating the grid, aisles, seats, and baggage compartments
    grid = [(i, j) for i in range(1, rows) for j in range(1, columns)] #all coordinates in the plane
    compartments = [(i, j) for i in range(1, rows) for j in compartment_columns] #coordinates of compartments for suitcases
    compartments2 = [Compartment(compartmentcapacity, compartment) for compartment in compartments] #creating the actual compartments
    aisle = [(i, j) for i in range(rows) for j in aislecolumns]  #coordinates for walkways
    seats = [(i, j) for i in range(rows) for j in seat_columns] #coordinates 
    seats2 = [Seats(seat) for seat in seats]
    #generating the space
    space = Space(grid, seats2, compartments2)
    return(space)
def generatepassengers(numboarding, space, seat_columns, aislecolumns): #generates a list of passengers in a random ordering
    passengers = []
    for i in range (numboarding):
        assigned_seat = [int(np.random.rand()*100), np.random.choice(seat_columns)]
        passengers.append(Passenger(assigned_seat, [0, np.random.choice(aislecolumns)], space))
    passenger_list = [i for i in range(numboarding)]
    random.shuffle(passenger_list)
    line = Boarding_Line([passengers[index] for index in passenger_list])
    return(line)

def simulate(numboarding, dimensions, layout, whileboarding = True, time = 100):
    space = generatespace(dimensions, layout) #generates the space the passengers act in
    line = generatepassengers(numboarding, space, layout[0], layout[2]) #generates list of randomly ordered passesngers
    t = 0
    if whileboarding == False:
        for t in range(time):
            passengers = line.seated + line.line
            history.record(passengers, space, t)
            line.update_line()
    elif whileboarding == True:
        while (len(line.line) > 0): #while some passengers aren't seated
            t = t + 1
            passengers = line.seated + line.line
            history.record(passengers, space, t)
            line.update_line()

#creating a Boarding line for simulation 1

print("__________________SIMULATION 1______________________")
simulate(numpassengers, [rows, totalcolumns], [seatcolumns, compartmentcolumns, aislecolumns], False, 100)

history.write(path, False, "round1passenger", "round1compartment", "round1seat")
history.clear()

print("__________________SIMULATION 2______________________")
simulate(numpassengers, [rows, totalcolumns], [seatcolumns, compartmentcolumns, aislecolumns])

history.write()
