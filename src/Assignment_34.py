#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    a=1
    c=0
    for i in num_list:
        for j in range(a,len(num_list)):
            sum1=0
            sum1=i+num_list[j]
            if(sum1==n):
                c+=1
        a+=1
    return c
            
num_list=[1, 2, 4, 5, 6]
n=7
print(find_pairs_of_numbers(num_list,n))