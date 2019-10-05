#PF-Tryout
def find_five_digit():
    str1=0
    for i in range(1,10):
        
        j=i-2
        k=j-2
        l=k-2
        m=l+2
        if(k+l+m==i):
            if(i+i+j==19):
                str1=i*10000+j*1000+k*100+l*10+m
                break
    
    return str1

print(find_five_digit())