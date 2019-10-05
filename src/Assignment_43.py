#PF-Assgn-43

def find_smallest_number(num):
    
    number=1
    factors=find_factors(number)
    while(1):
        if(len(factors)==num):
            break
        factors=[]
        number+=1
        factors=find_factors(number)
        
    return number
    
def find_factors(num):
    factors = [1]
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors
    
    
    

num=7
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)





    
   
