#PF-Assgn-41
def find_ten_substring(num_str):
    ten=[]
    for i in range(len(num_str)):
        if num_str[i]=='0':
            continue
        sum1=0
        
        for j in range(i,len(num_str)):
            sum1+=int(num_str[j])
            if sum1==10:
                ten.append(num_str[i:j+1])
    return ten
        
            
        
    
    
    
    
    
    
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)