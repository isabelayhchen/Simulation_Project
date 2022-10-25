import numpy as np

class Time:
    """
    Time still doesn't do much. Hasn't been tested yet.
    But the idea is that there is a time step in which the person in the front of the line gets seated.
    """

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

class Space: #need it to check if a tile is occupied. That's it
    def __init__(self, passenger_locations = []):
        self.passenger_locations = passenger_locations
    def is_occupied(self, coordinate):
        if self.passenger_locations.count(coordinate) == 0:
            return(False)
        else:
            return(True)
    def update_locations(self, newlocations):
        self.passenger_locations = newlocations