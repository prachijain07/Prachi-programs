#PF-Prac-8
def calculate_net_amount(trans_list):
    d=0
    w=0
    for i in trans_list:
        if(i[0]=="D"):
            d+=int(i[2:])
            
        else:
            w+=int(i[2:])
    net_amount=d-w
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))