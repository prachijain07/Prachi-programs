#PF-Assgn-36
def create_largest_number(number_list):
    str1=""
    new_list=sorted(number_list)
    new_list=new_list[::-1]
    for i in new_list:
        str1+=str(i)
    
    return int(str1)
    

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)