#PF-Assgn-38

def check_double(number):
    list1=[]
    list2=[]
    temp=2*number
    
    

    while(temp>0):
        a=temp%10
        list1.append(a)
        temp=temp//10
        
    
    
    while(number>0):
        a=number%10
        list2.append(a)
        number=number//10
    
    
    if(sorted(list1)==sorted(list2)):
        
        return True
    else:
        return False
    
    
print(check_double(125874))