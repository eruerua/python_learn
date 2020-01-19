def bouncingBall(h, bounce, window):
    n=0
    if h<=0:
        return -1
    if bounce>=1 or bounce<=0:
        return -1
    if window>=h:
        return -1
    while h>window:
        n += 1
        if n%2!=0:
            h=h*bounce
    return n

print(bouncingBall(30, 0.66, 1.5))