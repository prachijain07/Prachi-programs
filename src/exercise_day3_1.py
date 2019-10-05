#function to find factorial of a number
#function to check whether a number is palindrome or not 

def factorial(num):
    fact=1
    if(num==0):
        fact=1
        return
    
    while(num>0):
        fact=fact*num
        num=num-1
    return fact
    
    
def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
        
    if(temp==rev):
        print(temp,"number is palindrome")
    else:
        print(temp ,"number is not palindrome")
        
    
    
    
f=factorial(5)
print("factorial of a number is " , f)
palindrome(121)


    
