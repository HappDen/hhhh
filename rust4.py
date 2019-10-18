b = 0
y = 0 
d = 0
m = 0

for i in range (int(input())):
    x = int(input())
    if x / 2 == 1:
        y += 1
    elif x / 3 == 1:
        d += 1
    elif x / 1 == 1:
        b += 1
    elif x / 4 == 1:
        m += 1
if y < d and y < b and y < m:
    print(y*2)
elif d < y and d < b and d < m:
    print(d*3)
elif b < y and b < d and b < m:
    print (b)
elif m < y and m < b and m < d:
    print(m*4)
else: 
    print("lox")
