def dbl_linear(n):
    a=[1]
    x=0
    y=0
    for i in range(n+1):
        nextX=2*a[x]+1
        nextY=3*a[y]+1
        if nextX<=nextY:
            a.append(nextX)
            x+=1
            if nextX==nextY:
                y+=1
        else:
            a.append(nextY)
            y+=1
    return a[n]



import time
start = time.time()
print(dbl_linear(500000))
end = time.time()

print(end-start)
