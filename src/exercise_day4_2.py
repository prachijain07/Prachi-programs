#adding "sum" as key and sum of all salaries 
#in the existing dictionary

#we can also use it will work same
#for key,value in dict1.items():
    #sum1+=value

dict1={778028:50000,778029:20000,778030:25000,778031:55000}
sum1=0
for key in dict1:
    sum1+=dict1[key]
    
dict1.update({"SUM":sum1})
print(dict1)
    