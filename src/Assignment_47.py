#PF-Assgn-47
def encrypt_sentence(sentence):
    li1=[]
    li2=[]
    vowel=["a","e","i","o","u"]
    words=sentence.split(" ")
    
    for word in words[0::2]:
        rev=word[::-1]
        li1.append(rev)
        
    for word in words[1::2]:
        w=list(word)
        for i in range(0,len(w)-1):
            j=i+1
            if(w[i] in vowel and w[j] not in vowel):
                temp=w[i]
                w[i]=w[j]
                w[j]=temp
        str1=""
        for a in w:
            str1+=a
        
        li2.append(str1)
    a=0   
    l=[]
    while(a<len(li1) or a<len(li2)):  
        if(a<len(li1)):  
            l.append(li1[a])
        if(a<len(li2)):
            l.append(li2[a])
        a+=1
        
    str2=""
    for b in l:
        str2=str2+b+" "
    str2=str2[:-1]    
    return str2
    
    
            
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)