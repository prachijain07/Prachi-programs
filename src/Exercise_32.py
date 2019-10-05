#PF-Exer-32

def human_pyramid(no_of_people):
    if(no_of_people==1):
        return 1*(50)
    else:
        return no_of_people*(50)+human_pyramid(no_of_people-2)

    
def find_maximum_people(max_weight):
    no_of_people=0
    m=max_weight//50
    sum1=0

    
    for i in range(1,m+1,2):
        sum1+=i
        if(sum1>m):
            sum1=sum1-i
            break
    row=0
    for i in range(1,sum1+1):
        if(sum1//i==i):
            row=i
            break
    j=1
    for i in range(row):
        j+=2
    j-=2
    no_of_people=j
    return no_of_people


max_people=find_maximum_people(1000)
print(max_people)