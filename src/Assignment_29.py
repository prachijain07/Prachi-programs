#PF-Assgn-29
def calculate(distance,no_of_passengers):
    
    price_per_litre = 70
    mileage = 10
    price_ticket = 80
    
    profit=0
    
    total_earned = price_ticket*no_of_passengers
    total_spent = distance/mileage*price_per_litre
    
    if(total_earned>=total_spent):
        profit=total_earned-total_spent
        
    else:
        profit=-1
        
    return profit
        
    

    
    




distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))