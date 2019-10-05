#PF-Assgn-33

def find_common_characters(msg1,msg2):
    common=""
   
    for i in msg1:
        
        if(i==" "):
            continue
        
        elif i in common:
            continue
        
        else:
            if i in msg2:
                common+=i
                
        
    if(common==""):
        return -1 
        
            
    return common
    
    
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)