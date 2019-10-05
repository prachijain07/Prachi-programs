#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for i in word_list:
        a=len(i)
        count_list.append(a)
    
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))