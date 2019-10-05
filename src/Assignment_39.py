#PF-Assgn-39

menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0]

 
def place_order(*item_tuple):
    
    for i in range(0,len(item_tuple),2):
        ind=menu.index(item_tuple[i])
        
        if item_tuple[i] not in menu:
            print(item_tuple[i],"is not available")
            return
    
        
        elif(check_quantity_available(ind,item_tuple[i+1])==False):
            print(item_tuple[i],"stock is over")
            return
        
        else:
            print (item_tuple[i],"is available")
            
        
    
def check_quantity_available(index,quantity_requested):
    
    if(quantity_available[index]>=quantity_requested):
        quantity_available[index]-=quantity_requested
        return True
    else:
        return False
    
    
    
place_order("Fried Rice",2,"Soup",1)