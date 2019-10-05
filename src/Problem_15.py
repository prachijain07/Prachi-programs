#PF-Prac-15
def check_22(num_list):
    j=1
    for i in range(0,len(num_list)-1):
        
        if(num_list[i]==num_list[j] and num_list[i]==2):
            return True
        else:
            j+=1
    return False
        
print(check_22([3,2,5,1,2,1,2,2]))