#PF-Prac-5
def count_digits_letters(sentence):
    result_list=[]
    letter=0
    nums=0
    num_list=["1","2","3","4","5","6","7","8","9","0"]
    
    for i in sentence:
        if((i>="a" and i<="z") or(i>="A" and i<="Z")):
            letter+=1
        elif i in num_list:
            nums+=1
    result_list.append(letter)
    result_list.append(nums)
        
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))