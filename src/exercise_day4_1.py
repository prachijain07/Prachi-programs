#remove all duplicate characters from the string
#eg:input===popeye output==poey

def remove_dup(str1):

    str2=""

    for el in str1:
        if el in str2:
            continue
        else:
            str2+=el
        
        
    return str2


a="popeye"
b=remove_dup(a)
print(b)