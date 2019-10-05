#PF-Prac-10
def string_both_ends(input_string):
    length=len(input_string)
    
    if(length<2):
        return -1
    elif(length==2):
        return input_string+input_string
    else:
        return input_string[:2]+input_string[-2:]
        

input_string="w3w"
print(string_both_ends(input_string))