#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    price_per_plate=0
    delivery_chrge=0
    
    if(food_type=='N' and quantity_ordered>=1 and distance_in_kms>0):
        price_per_plate=150
        
    elif(food_type=='V' and quantity_ordered>=1 and distance_in_kms>0):
        price_per_plate=120
        
    else:
        bill_amount=-1
        return bill_amount
        
            
        
    if(distance_in_kms<=3):
        delivery_chrge=0
    elif(distance_in_kms>3 and distance_in_kms<=6):
        delivery_chrge=(distance_in_kms-3)*3
    else:
        delivery_chrge=3*3+(distance_in_kms-6)*6
        
        
    bill_amount = quantity_ordered * price_per_plate + delivery_chrge 
    
    return bill_amount


bill_amount=calculate_bill_amount("N",2,4)
print(bill_amount)