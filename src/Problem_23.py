#PF-Prac-23
def divisible_by_sum(number):
    sum1=0
    temp=number
    while(temp>0):
        a=temp%10
        sum1+=a
        temp=temp//10
    if(number%sum1==0):
        return True
    else:
        return False

    
number=42
print(divisible_by_sum(number))