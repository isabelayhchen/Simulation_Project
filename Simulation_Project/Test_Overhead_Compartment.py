"""
ovc = Overhead_Compartment(10, 3)
ovc.print_occupancy()
ovc.occupy_slot(3,2)
ovc.print_occupancy()
ovc.occupy_slot(3,2)
o = ovc.check_occupancy(2,2)
print(o)
"""
from Simulation_Project.Overhead_Compartment import Overhead_Compartment

ovc = Overhead_Compartment(10, 3)
ovc.print_occupancy()
two_C = ovc.convert_slot_to_seat(5) # 6th bin slot, which corresponds to seat 2C or (2,3)
print(two_C)

three_A = ovc.convert_slot_to_seat(6) # 7th bin slot, which corresponds to seat 3A or (3,1)
print(three_A)

three_B = ovc.convert_slot_to_seat(7) # 8th bin slot, which corresponds to seat 3B or (3,2)
print(three_B)

three_C = ovc.convert_slot_to_seat(8) # 9th bin slot, which corresponds to seat 3C or (3,3)
print(three_C)

ten_C = ovc.convert_slot_to_seat(29) # 30th bin slot, which corresponds to seat 10C or (10,3)
print(ten_C)