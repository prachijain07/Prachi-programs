#PF-Assgn-44

def find_duplicates(list_of_numbers):
    list_of_duplicates=[]
    
    
    for i in range(len(list_of_numbers)):
        k=i+1
        for j in range(k,len(list_of_numbers)):
            if(list_of_numbers[i]==list_of_numbers[j] and list_of_numbers[i] not in list_of_duplicates):
                list_of_duplicates.append(list_of_numbers[i])
    return list_of_duplicates
        
        
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)