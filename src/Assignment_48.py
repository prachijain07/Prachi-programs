#PF-Assgn-48

def find_correct(word_dict):
    correct_list=[]
    c=0
    ac=0
    w=0
    for key,value in word_dict.items():
        
        if(key==value):
            c+=1
        elif(len(key)!=len(value)):
            w+=1
        else:
            l=0
            for i in range(len(key)):
                if(key[i]!=value[i]):
                    l+=1
            if(l<=2):
                ac+=1
            else:
                w+=1
                
    correct_list.append(c)
    correct_list.append(ac)
    correct_list.append(w)     
    
    
    return correct_list           
    
                
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))