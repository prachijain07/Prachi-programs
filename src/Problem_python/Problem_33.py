#PF-Prac-33
def integer_to_english(number):
    
    dict_single_digit={1:"one",2:"two",3:"three",4:"four",5:"five"
    ,6:"six",7:"seven",8:"eight",9:"nine"}
    dict_tens={2:"twenty",3:"thirty",4:"forty",5:"fifty"
               ,6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    dict_after_ten={10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen"
                    ,15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    li=[10,11,12,13,14,15,16,17,18,19]
    
    if(number==1000):
        return "one thousand"
    elif(len(str(number))==1):
        return dict_single_digit[number]
    elif(number in li):
        return dict_after_ten[number]
        
    elif(number%100==0):
        a=number//100
        return dict_single_digit[a]+" hundred"
    elif(len(str(number))==2 and number//10>1):
        a=number//10
        b=number%10
        if(b==0):
            return dict_tens[a]
        return dict_tens[a]+" "+dict_single_digit[b]
    elif(len(str(number))==3):
        a=number//100
        b=number%10
        number=number//10
        m=number%10
        
        if(m==1):
            s=m*10+b
            return dict_single_digit[a]+ " hundred and "+dict_after_ten[s]
            
        return dict_single_digit[a]+ " hundred and "+dict_tens[m]+" "+dict_single_digit[b]
    
    else:
        return -1
    
            
number=212
print(integer_to_english(number))