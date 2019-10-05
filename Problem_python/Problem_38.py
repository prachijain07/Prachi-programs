#PF-Prac-38

def build_index_grid(rows, columns):
    a=""
   
    result_list=[]
    for i in range(rows):
        inner=[]
        for j in range (columns):
            a=str(i)+","+str(j)
            inner.append(a)
        result_list.append(inner)
        
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
small_index_grid = build_index_grid(1,1)
print(small_index_grid)
for i in result:
    print(i)