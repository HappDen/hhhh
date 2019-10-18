x = int(input())
i = 0
p = 0
l = 0
for i in range(x):
    beg = int(input())
    for l in range (beg):
        time, s = int(input()) , int(input())
        if beg == 1:
            y = s / time
        else:
            ah = s / time 
            p += ah
if y > p:
    print(p)
    print(y)
else:
    print(y)
    print(p)