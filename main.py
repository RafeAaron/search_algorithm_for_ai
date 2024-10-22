from NurseAllocationSystem import NurseAllocationSystem
from nurse import Nurse
from patient import Patient
import random

"""
Create 20 nurses that are going to be assigned patients
"""

nurses = []

for i in range(20):
    nurse = Nurse(i)
    nurses.append(nurse)

"""
Create 100 patients that are going to be assigned to nurses
"""

patients = []

for i in range(100):
    patients.append(Patient(random.randint(2, 10), False))

AllocationSystem = NurseAllocationSystem(nurses, patients)

nurses = AllocationSystem.allocatePatients()

"""
    List all the nurses in ascending order
"""
SortedNurses = AllocationSystem.sortAscending()

for i in range(20):
    print(SortedNurses[i])