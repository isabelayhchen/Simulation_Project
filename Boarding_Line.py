import numpy as np
import Passenger
import Time 

class Boarding_Line:
    """
    Boarding Line considers part of the line that is in the airplane and the part that is still out of the door.
    """

    def __init__(self, line, locations = []):
        self.line = line # number of customers waiting in the aisle
        row = 0 - len(line) #'negative' coordinates to make the code work, could represent queueing outside the plane..
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

    def update_line(self, step = [1, 1], time = 0): #updates the line as all passengers move forward in one time-step, replacement for 'one sitting step' function
        passengers_removed = 0
        tstep = 0
        for passenger in self.line:
            passenger.move()
            if passenger.is_seated() == True: #if a passenger is seated, remove them from the list of queues
                passengers_removed = passengers_removed + 1
                self.line.remove(passenger)
        print("The new aisle line is:\n")
        print(self.line)
        print(passengers_removed, "passengers sat down in this step")