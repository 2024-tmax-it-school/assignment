value=[10,8,6,5,12,7]
for i in range(len(value)) :
    for j in  range(i+1,len(value)):
        if value[i]>value[j] :
            value[j],value[i]=value[i],value[j]
print(value)