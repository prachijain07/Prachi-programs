#PF-Prac-7
def seed_no(number,ref_no):
    temp=number
    f=1
    while(number>0):
        i=number%10
        f=f*i
        number=number//10
    if(ref_no==temp*f):
        return True
    else:
        return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))