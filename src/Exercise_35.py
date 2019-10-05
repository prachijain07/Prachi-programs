#PF-Exer-35

def count_names(name_list):
    count1=0
    count2=0
    
    for name in name_list:
        
        if(name.endswith("at") and len(name)==3):
            count1+=1
        if(name.find("at")>=0):
            count2+=1
    
    
    
    print("_at -> ",count1)
    print("%at% -> ",count2)


#Provide different names in the list and test your program
name_list=["Hat","Cat","rabbit","matter"]
count_names(name_list)