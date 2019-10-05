#PF-Exer-34
import math
def find_number_of_combination(number_of_flavours):
    total_combination=0
    for i in range(1,number_of_flavours+1):
        total_combination+=math.factorial(number_of_flavours)//(math.factorial(i)*
                                                                math.factorial(number_of_flavours-i))
    
    
    return total_combination+1

number_of_combination=find_number_of_combination(6)
print(number_of_combination)