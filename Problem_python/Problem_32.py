#PF-Prac-32
def check_squares(number):
    for i in range(number,0,-1):
        for j in range(0,number+1):
            if((i*i+j*j)==number):
                return True
                
    return False
                
number=68
print(check_squares(number))