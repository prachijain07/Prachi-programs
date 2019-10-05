#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    
    li=patient_medical_speciality_list[1::2]
    p=0
    o=0
    e=0
    
     
    for el in li:
        if(el=='P'):
            p+=1
        elif(el=='O'):
            o+=1
        else:
            e+=1
            
    if(p>o and p>e):
        speciality=medical_speciality["P"]
        
    elif(o>p and o>e):
        speciality=medical_speciality["O"]
        
    else:
        speciality=medical_speciality["E"]
        
         
    return speciality



patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)