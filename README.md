# AI Greedy Best First Algorithm For Patient Allocation To Doctors

Problem:
	    In a populated area, we have recently had a surge in the number of patients in a hospital/clinic. The patients are placed on the hospital floor and their number is large compared to the available nurses. There have been complaints that the nurses give some patients more attention compared to others thus we have been tasked with finding an appropriate solution to this problem. Keep in mind that the number of patients varys daily.
	
Goal:
		To develop a n algorithm that can allocate the nurses on the hospital floor to a group of patients so that all patients receive nearly equal attention from the nurses whilst they are on the hospital floor.
		
Formally define the problem:
		State: A specific nurse is allocated to a specific number of unique patients.
		
		Initial State: No nurse has a patient allocated to them and no patient has a nurse they are allocated to
		
		Actions: Add a patient to a nurse if this will minimize the cost 
		
		Transition model: Returns a grouping of nurses with an associated grouping of patients.
		
		Goal test: All patients are allocated to one of the nurses.
		
		Path cost: Every hour spent on a patient would add a singular unit to the cost. So the path cost is the number of hours spent on all the patients.
		
State an appropriate search strategy and provide justification for your choice.
		For this problem, we have decided to use the greedy best first search strategy. This is because we know the various hours to be spent on every patient at the time of allocation. But we don't know the desired outcomes in terms of allocation, whether to allocate the patients that need the most amount of care or the least amount of care. Therefore our algorithm prioritizes nurses with the least workload in the group and allocates a patient basing on how many working hours the nurse has already, with the least nurse, recieving priority.
		
Demonstrate how the said search strategy would lead to a solution to the described problem
		The algorithm would first start by taking in a list of patients and nurses. The patients will then be allocated to the nurses basing on how many hours they have already been allocated. This means that nurses with the least work hours will be selected in a greedy fashion. When all the patients have been allocated the search stops and the list of allocations is returned. It can then be sorted and further processed to produce relevant information.