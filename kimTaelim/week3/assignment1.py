g = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random
# g.append(random.randint(0, 9))  append 말고 다른거
# 파이썬 리스트 객체 검색
# remove

for x in range(random.randint(0, 9)):
    for y in range(x, random.randint(0, 9)):
        if g[x] > g[y]:
            g[x], g[y] = g[y], g[x]

print(g)