#PF-Assgn-16

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    f=rupees_to_make//5
    o= rupees_to_make%5
  
    if(f<=no_of_five):
        if(o<=no_of_one):
            five_needed=f
            one_needed=o
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
            
    else:
        f_more_needed=f-no_of_five
        if(no_of_one>=o+f_more_needed*5):
            five_needed=no_of_five
            one_needed=o+f_more_needed*5
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
            
            
            
        
        
    

    
    


make_amount(28,8,5)