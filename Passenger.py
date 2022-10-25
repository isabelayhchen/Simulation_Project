import numpy as np
import Time
class Passenger:
    """
    Passenger is a class that describes passengers.

    Input: (row, col) of where the passenger is seated.

    For now, there are 3 columns: A (1), B (2), C(3).
    Rows can range from [1, infinity].

    Examples:
        Passenger sitting at 1A = Passenger(1, 1)
        Passenger sitting at 7B = Passenger(7, 2)
        Passenger sitting at 12C = Passenger(12, 3)

    Future Ideas:
    Passenger should start including Time instances.
    Boarding Groups.
    Denoting whether they are seated or not.
    """

    def __init__(self, assigned_seat, location, space, walking_speed = 1, sit = False):
        self.assigned_seat = assigned_seat #2x1 coordinates
        self.location = location
        self.walking_speed = walking_speed
        self.seating_status = sit
        self.space = space
    def is_seated(self, exact = False):
        if exact == True:
            if self.location == self.assigned_seat: #this is for when we finally simulate passengers putting their shit away
                return(True)
            else:
                return(False)
        else:
            if self.location[0] == self.assigned_seat[0]: #if passengers are in the same row
                return(True)
            else:
                return(False)
    def update_location(self, newlocation):
        self.location = newlocation
    def print_(self):
        c = self.assigned_seat[1]
        if c == 1:
            c = 'A'
        elif c == 2:
            c = 'B'
        else:
            c = 'C'
        print("Passenger", self.assigned_seat[0], self.assigned_seat[1])
    def get_seat_row(self):
        return self.assigned_seat[0]
    def move(self, step = [1, 1]): #does this for one time-step right now, makes the passenger either take a seat or move one row down, or wait (if someone is in-front of them)
        cost = 0
        newlocation = [self.location[0] + step[0]*self.walking_speed, self.location[1] + step[1]*self.walking_speed] #so that we can scale with walking speed
        if self.location[0] == self.assigned_seat[0]:
            self.seating_status = True
            self.location = self.assigned_seat
        elif self.space.is_occupied(newlocation) == True:
            pass
        else:
            self.location = newlocation
        if self.location[0] > self.assigned_seat[0]: #will be used to simulate the line "freezing" as the passenger finds their way to the seat
            cost = (self.location[0] - self.assigned_seat[0])

    
