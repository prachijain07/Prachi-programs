#PF-Tryout

def find_new_salary(current_salary,job_level):
    if(job_level==3):
        hike=15
    elif(job_level==4):
        hike=7
    elif(job_level==5):
        hike=5
    else:
        hike=0
    
    new_salary=current_salary+current_salary*hike/100

    return new_salary

new_salary=find_new_salary(10000,6)
print(new_salary)