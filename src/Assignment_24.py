#PF-Assgn-24
def form_triangle(num1,num2,num3):
    
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    if((num1+num2>num3) and (num1+num3>num2) and (num3+num2>num1)):
        return success
    else:
        return failure
        
    
    
    
num1=3
num2=3
num3=5
form_triangle(num1, num2, num3)