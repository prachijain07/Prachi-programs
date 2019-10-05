#PF-Tryout

def generate_next_date(day,month,year):
    next_month=month
    next_day=day
    next_year=year
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        
        if(day==31 and month==12):
            next_month=1
            next_day=1
            next_year=year+1
        elif(day==31):
            next_month=month+1
            next_day=1
        else:
            next_day=day+1
            
            
    elif(month==2):
        if((year%4==0 and year%100!=0) or year%400==0):
            
            if(day==29):
                
                next_month=month+1
                next_day=1
            else:
                next_day=day+1
        
        else:
            
            if(day==28):
                
                next_month=month+1
                next_day=1
            else:
                next_day=day+1
    
    else:
        if(day==30):
            next_month=month+1
            next_day=1
        else:
            next_day=day+1
        
            
            
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(25,4,2015)