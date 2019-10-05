#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    if(no_of_passengers<=5):
        for i in range(no_of_passengers):
            j=101+i
            m=airline+":"+source[0:3]+":"+destination[0:3]+":"+str(j)
            ticket_number_list.append(m)
            
    else:
        a=no_of_passengers-5
        for i in range(a,no_of_passengers):
            j=101+i
            m=airline+":"+source[0:3]+":"+destination[0:3]+":"+str(j)
            ticket_number_list.append(m)
        
            
    return ticket_number_list


print(generate_ticket("AI","Bangalore","London",7))