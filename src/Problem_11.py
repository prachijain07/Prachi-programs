#PF-Prac-11
def find_upper_and_lower(sentence):
    result_list=[]
    u=0
    l=0
    for i in sentence:
        if(i==" "):
            continue
        elif(i>="A" and i<="Z"):
            u+=1
        elif(i>="a" and i<="z"):
            l+=1
            
    result_list.append(u)
    result_list.append(l)
       
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))