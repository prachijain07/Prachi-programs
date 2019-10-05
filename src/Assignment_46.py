#PF-Assgn-46

def nearest_palindrome(number):
    i=number+1
    while(1):
        
        temp=i
        j=0
        pal=0
        while(temp>0):
            a=temp%10
            pal=10*pal+a
            temp=temp//10
  

        if(pal==i):
            return i
        i+=1
    
number=12300
print(nearest_palindrome(number))