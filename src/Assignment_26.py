#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    legs_left=legs-(heads*2)
    
    if(heads>legs):
         print(error_msg)
         
        
    
    elif(legs_left%2!=0):
         print(error_msg)
         
         
    else:
        rabbit_count=legs_left//2
        chicken_count=heads-rabbit_count
        print(chicken_count,rabbit_count)
    


solve(35,94)