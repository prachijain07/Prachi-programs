#PF-Assgn-50

def sms_encoding(data):
    words=data.split(" ")
    vowel=["a","e","i","o","u","I","E","A","O","U"]
    str1=""
    for word in words:
        l_word=list(word)
        c=0
        for i in l_word:
            if i in vowel:
                c+=1
        if(c==len(l_word)):
            str1+=word+" "
        else:
            str2=""
            for i in word:
                if i not in vowel:
                    str2+=i
                    
            str1+=str2+" "
            
    return str1[:-1]
        
                
data="I love Python"
print(sms_encoding(data))