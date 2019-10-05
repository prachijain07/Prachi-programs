#PF-Prac-21
def check_numbers(num1,num2):
    count=0
    num_list=[]
    for j in range(num1+1,num2+1):
        for i in range(num1,j):
            if(j>i and j%i==0):
                count+=1
                num_list.append(j)
                break
                    
    num_list=set(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))