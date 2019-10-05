#factors of a number
#find whether a number is a perfect number or not
#print even number from 1-20 (20 inclusive)




def factors(num):
    print("factors of a ",num," is")
    
    for i in range(1,num+1):
    
        if(num%i==0):
            print(i)
            
def perfect(num):
    
    sum=0
    for i in range(1,num):
    
        if(num%i==0):
            sum=sum+i
        
    if(num==sum):
        print(num," is perfect number")
    else:
        print(num," is not perfect number")
        

    
    
    
factors(6)

print("Even number from 1-20 inclusive is:")
for i in range(2,21,2):
    print(i)
    
    
perfect(6)