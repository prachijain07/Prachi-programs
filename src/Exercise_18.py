#PF-Exer-18

def get_count(num_list):
    count=0
    j=0

    for i in range(1,len(num_list)):
        
        if(num_list[j]==num_list[i]):
            count+=1
            j+=1
        else:
            j+=1
            
            

    return count


num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))