#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    while(number>0):
        a=number%10
        sum_of_digits=sum_of_digits+a
        number=number//10
    
    return sum_of_digits


sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          