val = [5, 6, 7, 8, 1, 4]


# a,b = b,a

for x in range(len(val)):
    for y in range(x, len(val)):
        if val[x] > val[y]:
            val[x], val[y] = val[y], val[x]

print(val)
    
