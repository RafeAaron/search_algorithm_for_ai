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
    patients.append(Patient(random.randint(1, 20), False))

AllocationSystem = NurseAllocationSystem(nurses, patients)

nurses = AllocationSystem.allocatePatientsBasic()

"""
    List all the nurses in ascending order
"""
SortedNurses = AllocationSystem.sortNursesAscending()
SortedPatients = AllocationSystem.sortPatients()

for i in range(20):
    print(SortedNurses[i])

for i in range(len(patients)):
    print(SortedPatients[i])

