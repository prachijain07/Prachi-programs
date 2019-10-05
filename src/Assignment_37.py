#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum1=0
    for i in chocolates_received:
        sum1+=i
    return sum1
    
    
    
def reward_child(child_id_rewarded,extra_chocolates):
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
        return
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
        return
    else:
        ind=child_id.index(child_id_rewarded)
        chocolates_received[ind]+=extra_chocolates
    print(chocolates_received)
    

        
        
   




    
    
    


print(calculate_total_chocolates())
reward_child(20,2)