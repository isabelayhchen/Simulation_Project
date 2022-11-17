import numpy as np


class Overhead_Compartment:

    num_of_bins = 0
    bins = [] # represents bin slots on top of a certain row. E.g. Bin slot 2A
    occupancy = [] # 0 or 1, represents whether a slot is occupied or not

    def __init__(self, num_of_rows, num_of_cols):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.num_of_slots = self.create_slots() # initialize bins
        self.occupancy = np.zeros([self.num_of_rows, self.num_of_cols])


    def create_slots(self):
        """
        Initializes the bins based on rows, columns and realistic space in airplanes.
        :return:
        """
        num_of_slots = self.num_of_rows * self.num_of_cols
        return num_of_slots

    def occupy_slot(self, bin_slot_row, bin_slot_col):
        if self.check_occupancy(bin_slot_row,bin_slot_col):
            print("Slot", bin_slot_row, bin_slot_col, "is already occupied.")
            return
        else:
            self.occupancy[bin_slot_row-1][bin_slot_col-1] = 1
        return

    def convert_row_col_to_slot(self, row, col):
        return row*col-1 # decrease 1 because python index starts at zero

    def print_occupancy(self):
        print(self.occupancy)

    def check_occupancy(self, row, col):
        return self.occupancy[row-1][col-1]

ovc = Overhead_Compartment(10, 3)
ovc.print_occupancy()
ovc.occupy_slot(3,2)
ovc.print_occupancy()
ovc.occupy_slot(3,2)
o = ovc.check_occupancy(2,2)
print(o)