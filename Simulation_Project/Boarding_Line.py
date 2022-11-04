import numpy as np
import Passenger
import World 

class Boarding_Line:
    """
    Boarding Line considers part of the line that is in the airplane and the part that is still out of the door.
    """

    def __init__(self, line, locations = []):
        self.passengers = line
        self.line = line # number of customers waiting in the aisle
        row = 0 - len(line) #'negative' coordinates to make the code work, could represent queueing outside the plane..
        self.seated = []
        if locations == []: #forms initial line of passengers, setting all column coordinates to 0 for now since we're not considering columns
            for passenger in line:
                row += 1
                passenger.update_location([row, 0])
        else:
            pass
    def add_passenger(self, cust):
        """ Adds a customer to the end of the boarding line.
        """
        self.line = np.append(self.line, cust)
    def get_queue(self):
        return([passenger.name for passenger in self.line])
    def get_seated(self):
        return([passenger.name for passenger in self.seated])
    def update_line(self): #updates the line as all passengers move forward in one time-step, replacement for 'one sitting step' function
        passengers_removed = 0
        for passenger in self.line:
            passenger.move()
            if passenger.seating_status == True: #if a passenger is seated, remove them from the list of queues
                passengers_removed = passengers_removed + 1
                self.line.remove(passenger)
                self.seated.append(passenger)