from nurse import Nurse
from patient import Patient

import random

##This is the class that caters for the
##allocation of nurses and patients as well as
##sorting methods for the classes
class NurseAllocationSystem:

    def __init__(self, list_of_nurses, list_of_patients):
        self.list_of_nurses = list_of_nurses
        self.list_of_patients = list_of_patients

    def sortNursesAscending(self):

        num_nurses = len(self.list_of_nurses)

        for i in range(num_nurses):

            least = self.list_of_nurses[i].getTotalWorkHours()
            change = False
            leastNurse = self.list_of_nurses[i]
            leastNurseIndex = i

            for a in range(num_nurses):
                if i == a or a < i:
                    continue

                else:
                    if self.list_of_nurses[a].getTotalWorkHours() < least:
                        least = self.list_of_nurses[a].getTotalWorkHours()
                        leastNurse = self.list_of_nurses[a]
                        leastNurseIndex = a
                        change = True
                
            if change == False:
                continue

            else:
                tempNurse = self.list_of_nurses[i]
                self.list_of_nurses[i] = leastNurse
                self.list_of_nurses[leastNurseIndex] = tempNurse
        
        return self.list_of_nurses
    
    def getAllPatients(self):
        return self.list_of_patients
    
    def getAllNurses(self):
        return self.list_of_nurses
    
    def allocatePatientsBasic(self):
        number_of_patients = len(self.list_of_patients)
        number_of_nurses = len(self.list_of_nurses)

        for i in range(number_of_patients):
            self.list_of_nurses[i % number_of_nurses].addPatient(self.list_of_patients[i])
            self.list_of_nurses[i % number_of_nurses].setTotalWorkHours(self.list_of_patients[i].getTimeRequired())

        return self.list_of_nurses
    
    def sortPatientsAscending(self):

        num_patients = len(self.list_of_patients)

        for i in range(num_patients):

            least = self.list_of_patients[i].getTimeRequired()
            change = False
            leastNurse = self.list_of_patients[i]
            leastNurseIndex = i

            for a in range(num_patients):
                if i == a or a < i:
                    continue

                else:
                    if self.list_of_patients[a].getTimeRequired() < least:
                        least = self.list_of_patients[a].getTimeRequired()
                        leastNurse = self.list_of_patients[a]
                        leastNurseIndex = a
                        change = True
                
            if change == False:
                continue

            else:
                tempNurse = self.list_of_patients[i]
                self.list_of_patients[i] = leastNurse
                self.list_of_patients[leastNurseIndex] = tempNurse
        
        return self.list_of_patients
    
    def allocatePatientsGreedyApproach(self):
        for i in range(len(self.list_of_patients)):

            nurseWithLeastWorkLoad = self.list_of_nurses[0]
            nurseWithLeastWorkLoadIndex = 0

            for a in range(len(self.list_of_nurses)):
                if self.list_of_nurses[a].getTotalWorkHours() <= nurseWithLeastWorkLoad.getTotalWorkHours():
                    nurseWithLeastWorkLoad = self.list_of_nurses[a]
                    nurseWithLeastWorkLoadIndex = a

                else:
                    continue

            self.list_of_nurses[nurseWithLeastWorkLoadIndex].addPatient(self.list_of_patients[i])

        return self.list_of_patients
