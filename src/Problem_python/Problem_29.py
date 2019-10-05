#PF-Prac-29
def exchange_list(number_list):
    li=[]
    last=len(number_list)//2
    li=number_list[-1:last-1:-1]+number_list[0:last]
    number_list=li

    
    return number_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))