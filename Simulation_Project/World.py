class Time:
    h = 1 # time step
    walking_time_unit_per_row = 1 # second

    def __init__(self):
        self.time = 0

    def advance_one_time(self):
        self.time += self.h

    def print_(self):
        print(self.time)

    def get_time(self):
        return self.time

class Seats: 
    #TODO: define the "Seats" class
    def __init__(self, location, name = "null"):
        if name == "null":
            self.name = location
        else:
            self.name = name   
        self.location = location
        self.status = 'empty'
    def fill(self):
        if self.status == 'full':
            return('denied: occupied')
        else:
            self.status = 'full'
            return('passenger seated')

class Compartment:
    #TODO: right now 'compartments' are points in space with nebolous 'capacities'. Make this represent an actual thing in real life (will need 'baggages' class)
    def __init__(self, capacity, location, name = "null"):
        if name == "null":
            self.name = location
        else:
            self.name = name
        self.capacity = capacity 
        self.location = location
        self.load = 0
        self.status = 'Open'
    def stow(self):
        if self.status == 'Open':
            self.load = self.load + 1
            if self.load < self.capacity:
                pass
            else:
                self.status = 'Closed'
            return('stowed')
        else:
            return('not stowed: fully occupied')
        
class Space: #need it to check if a tile is occupied. That's it
    def __init__(self, grid, seats, compartments, passenger_locations = []):
        self.grid = grid
        self.passenger_locations = passenger_locations 
        self.opencompartments = {}
        self.openseats = {}
        self.compartment_locations = []
        for compartment in compartments:
            compartment.name = compartment.location
            self.opencompartments[compartment.location] = compartment
            self.compartment_locations.append(compartment.location)
        for seat in seats:
            seat.name = seat.location
            self.openseats[seat.location] = seat
        self.closedseats = {}
        self.closedcompartments = {}
    def is_occupied(self, coordinate):
        if self.passenger_locations.count(coordinate) == 0:
            return(False)
        else:
            return(True)
    def updateinfo(self, newlocations): #records which seats and compartments are fully occupied and which aren't
        for seat in self.openseats: 
            if seat.status == 'Closed': 
                self.closedseats[seat.location] = seat
                del self.openseats[seat.location]
            elif seat.status == 'Open':
                pass
        for seat in self.closedseats: 
            if seat.status == 'Open': 
                self.openseats[seat.location] = seat
                del self.closedseats[seat.location]
            elif seat.status == 'Closed':
                pass
        for compartment in self.opencompartments: 
            if compartment.status == 'Closed': 
                self.closedcompartments[compartment.location] = compartment
                del self.opencompartments[compartment.location]
            elif compartment.status == 'Open':
                pass
        for compartment in self.closedcompartments: 
            if compartment.status == 'Open': 
                self.opencompartments[compartment.location] = compartment
                del self.closedcompartments[compartment.location]
            elif compartment.status == 'Closed':
                pass
        self.passenger_locations = newlocations
        
class vector: #to make some of the passenger functions easier to implement
    def add(a, b):
        return([a[i] + b[i] for i in range(0, len(a))])
    def mult(a, b):
        return([a[i] * b[i] for i in range(0, len(a))])
    def scalmult(l, a):
        return([a[i] * l for i in range(0, len(a))])
    def elmpow(a, n):
        return([numb ** n for numb in a])
    def eucnorm(a):
        return(sum(vector.elmpow(a, 2))**0.5)
    def normal(a):
        norma = vector.scalmult(1/vector.eucnorm(a), a)
        return(norma)
    def subtract(a, b):
        return([a[i] - b[i] for i in range(0, len(a))])

class ErrorMessages:
    def passengererrormessage(passenger, time, message):
        print(" passenger: " + str(message))