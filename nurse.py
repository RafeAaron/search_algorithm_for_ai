##Nurse Data Structure
##Below is the data structure of the nurse as well as it's features
##It only takes in an id and the rest is done internally

class Nurse:

    def __init__(self, id):
        self.assignedPatients = []
        self.totalWorkHours = 0
        self.count = 0
        self.id = id

    def getID(self):
        return self.id

    def getTotalWorkHours(self):
        return self.totalWorkHours

    def setTotalWorkHours(self, newTotal):
        self.totalWorkHours += newTotal

    def addPatient(self, patient):
        self.assignedPatients.append(patient)
        self.count += 1
        self.setTotalWorkHours(patient.getTimeRequired())

    def count(self):
        return self.count

    def __str__(self):
        return f"Nurse #{self.id} has {len(self.assignedPatients)} patient(s) with a total of {self.totalWorkHours} total work hours"