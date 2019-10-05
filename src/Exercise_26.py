#PF-Exer-26

def factorial(number):
    f=1
    if(number==0):
        f=1
    else:
        while(number>0):
            f=f*number
            number=number-1
    return f


def find_strong_numbers(num_list):
    strong_num_list=[]
    for num in num_list:
        if num==0:
            continue
        i=num
        sum1=0
        
        while(i>0):
            rem=i%10
            sum1=sum1+factorial(rem)
            i=i//10
        
        if(sum1==num):
            strong_num_list.append(num)
    
    return strong_num_list
            
            
            


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)