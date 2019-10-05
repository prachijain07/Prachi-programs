#PF-Prac-31
def sum_of_elements(num_list,number):
    
    li=num_list
    
    for i in range (0,len(num_list)):
        if li[i]==number:
            if li.index(li[i])!=0:
                li[i-1]=0
            if(li.index(li[i])!=len(num_list)-1):
                li[i+1]=0
            li[i]=0
    
    result_sum=0        
    for j in li:
        result_sum+=j
            
    return result_sum
      
num_list=[1,7,3,4,1,7,10,5]
number=7
print(sum_of_elements(num_list, number))