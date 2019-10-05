#PF-Prac-2
def bracket_pattern(input_str):
    opn=0
    cls=0
    if(input_str[0]=="(" and input_str[-1]==")"):
        for i in input_str:
            if(i=="("):
                opn+=1
            else:
                cls+=1
        if(opn==cls):
            return True
        else:
            return False
    else:
        return False

    
input_str="(())("
print(bracket_pattern(input_str))