import World
class Baggage:
    #TODO: define a class for baggage
    pass
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

    def __init__(self, assigned_seat, location, space, name = "null", walking_speed = 1, stowedluggage = False, approachedseat = False, sit = False):
        if name == "null":
            self.name = assigned_seat
        else:
            self.name = name
        self.assigned_seat = assigned_seat #2x1 coordinates
        self.location = location
        self.velocity = walking_speed
        self.seating_status = sit
        self.space = space
        self.stowedluggage = stowedluggage
        self.approachedseat = approachedseat
    #functions that return information
    def update_location(self, newlocation):
        self.location = newlocation
    def get_seat_row(self):
        return self.assigned_seat[0]
    def get_info(self):
        info = [self.location, self.assigned_seat, self.seating_status, self.stowedluggage, self.velocity]
        return(info)
    #elementary functions
    def step(self, direction):
        newlocation = World.vector.add(self.location, World.vector.scalmult(self.velocity, World.vector.normal(direction)))
        self.location = newlocation
    def stow(self, compartmentlocation):
        try: #see if the compartment in question is open
            compartment = self.space.opencompartments[compartmentlocation]
            compartment.stow()
            self.stowedluggage = True
        except KeyError: #if not, then the compartment is full
            pass
    def sit(self):
        try: #see if the compartment in question is open
            seat = self.space.openseats[tuple(self.location)]
            seat.fill() #recording that the seat is now occupied
            self.seating_status = True #recording that the passenger sat down
        except KeyError: #if not, then the compartment is full
            message = "Error: seat is occupied/doesn't exist"
            World.ErrorMessages.passengererrormessage(self, message)
    
    #simple functions that (each) perform a specific sub-task
    def approachseat(self):
        direction = [self.assigned_seat[0] - self.location[0], 0] #just move down the row
        self.step(direction)
        if self.approachedseat == False and self.location[0] == self.assigned_seat[0]:
            self.approachedseat = True
    def placeluggage(self):
        #if there is a compartment in the same row as the current passenger, consider that compartment
        compartments_in_row = [compartment for compartment in self.space.compartment_locations if compartment[0] == self.location[0]]
        for compartment in compartments_in_row: #tries to stowe luggage in all compartments that are on the same row as the passenger
            self.stow(compartment)
            if self.stowedluggage == True:
                break
            else:
                pass
        if self.stowedluggage == False: #if passenger still hasn't stowed their luggage, move one row down
            self.step([1, 0])
    def sitdown(self): #now that passenger has found their seat, stowed their luggage, and returned to their seat, they sit down
        if self.stowedluggage == False: #first a quick check
            World.ErrorMessages.passengererrormessage(self, "ERROR: sitdown called before passenger stowed luggage")
        if self.location == self.assigned_seat:
            self.sit()
        elif self.location[0] == self.assigned_seat[0]:
            direction = [0, self.assigned_seat[1] - self.location[1]]
            self.step(direction)
        else:
            self.approachseat()
    def get_up(): #TODO
        pass
    #the function that puts everything together
    def move(self): #does this for one time-step right now, makes the passenger either take a seat or move one row down, or wait (if someone is in-front of them)
        if self.stowedluggage == True:
            self.sitdown()
        elif self.stowedluggage == False and self.approachedseat == True:
            self.placeluggage()
        elif self.stowedluggage == False and self.approachedseat == False:
            self.approachseat()
        else:
            message = 'Error: this scenario shouldnt exist'
            World.ErrorMessages.passengererrormessage(self, message)

    
