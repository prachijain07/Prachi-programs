#PF-Prac-20
def ducci_sequence(test_list,n):
    
    final_list=[]
    l=test_list
    a=n+1
    
    while(a!=0):
        
        li=[]
        j=1
        for i in l:
            if(j<4):
                li.append(abs(l[j]-i))
                j+=1
            else:
                li.append(l[3]-l[0])
    
        l=li
        final_list.append(li)
        a-=1
    
    return final_list[n]

ducci_element=ducci_sequence([7,60,861,3070] , 3)
print(ducci_element)