#PF-Prac-16
def rotate_list(input_list,n):
    
    output_list=[]
    
    if(len(input_list)>n):
        output_list=input_list[-n:]+input_list[:-n]
            
    else:
        output_list=input_list
          
            
    return output_list

input_list= [10,20,30,40,50]
output_list=rotate_list(input_list,2)
print(output_list)