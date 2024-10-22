"""
Program Name: AI allocation of patients to nurses
Authors:
    Nantumbwe Prossy K
    Nakimbugwe Edith
    Nejesa Sandrine
    Opio George Micheal
    Rubangakene Stuart

Description:
    A simple allocation program that illustrates how nurses can be 
    allocated patients given that the time to work upon patients is
    already known as well as their number

Date: 21/10/2024
"""

#These are imports for the various data 
#structures we have designed that are necessary
#for the solving the problem

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
All patients should have a random number of hours that they take to be worked on
"""

patients = []

for i in range(100):
    patients.append(Patient(random.randint(1, 30), False))

#Create an instance of the allocation system to allow us efficiently allocate
#patients based on their workloads(Time taken to cater to a patient)
AllocationSystem = NurseAllocationSystem(nurses, patients)

#Run an allocation to see the allocations that will be made
#given the nurses present and the patients available
nurses = AllocationSystem.allocatePatientsGreedyApproach()

"""
    Sort all the nurses and patients in ascending order
    Feel free to implement descending order
"""
SortedNurses = AllocationSystem.sortNursesAscending()
SortedPatients = AllocationSystem.sortPatientsAscending()

##Implement a for loop to view both the patients
##And the nurses sorted in ascending order of duration