#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum1=0
    c=0
    for i in list_of_marks:
        sum1+=i
        
    avg=sum1/10
    for i in list_of_marks:
        if(i>avg):
            c+=1
    percentage=c*100/10
    return percentage
        
  

def sort_marks():
    a=generate_frequency()
    c=0
    li=[]
    for i in a:
        if(i==0):
            c+=1
        else:
            while(i>=1):
                i-=1
                li.append(c)
            c+=1
    return li
            
    

def generate_frequency():
    freq=[]
    
    for i in range(0,26):
        f=0
        for j in list_of_marks:
            if(j==i):
                f+=1
        freq.append(f)
    return freq
            
        

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())