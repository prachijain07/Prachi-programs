#PF-Prac-24
def find_gcd(num1,num2):
    if(num1<num2):
        temp=num1
        num1=num2
        num2=temp
    for i in range(1,num2+1):
        if(num1%i==0 and num2%i==0):
            gcd=i
            
    return gcd
    
num1=45
num2=9
print(find_gcd(num1,num2))