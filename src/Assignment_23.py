#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    
    for j in range(0,len(reqd_gems)):    
        c=0
        for i in range(0,len(gems_list)):
        
            if(gems_list[i]==reqd_gems[j]):
                bill_amount+=price_list[i]*reqd_quantity[j]
                c=1
        
        if(c==0):
            bill_amount=-1
            return bill_amount
    
    if(bill_amount>30000):
        discount=0.05*bill_amount
        bill_amount=bill_amount-discount
        
                
        
            

    
                
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]


price_list=[1760,2119,1599,3920,3999]


reqd_gems=["Ivory","Emerald","Garnet"]


reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list,price_list,reqd_gems,reqd_quantity)
print(bill_amount)