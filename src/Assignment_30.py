#PF-Assgn-30

def encode(message):
    encoded_message=""
    i=0
    j=1
    count=1
    
    while(j<len(message)):
        
        
        if(message[i]==message[j]):
            count+=1
            i+=1
            j+=1
        
        else:
            encoded_message+=str(count)+message[i]
            count=1
            i+=1
            j+=1
            
    encoded_message+=str(count)+message[i]
            
    return encoded_message
            
        
        
    


encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)