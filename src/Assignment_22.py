#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years=[]
    i=1
    while(i<=15):
        if((given_year%4==0 and given_year%100!=0) or given_year%400==0):
            list_of_leap_years.append(given_year)
            given_year+=4
            i+=1
        
        else:
            given_year+=1
            

    return list_of_leap_years

list_of_leap_years=find_leap_years(1784)
print(list_of_leap_years)