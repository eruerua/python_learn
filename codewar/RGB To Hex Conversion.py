def rgb(r, g, b):
    s=''
    for i in [r,g,b]:
        if i<10:
            s+='0'
        if i <= 0:
            i=0
        if i > 255:
            i=255
        s+=hex(i)[2:]
    return s.upper()

print(rgb(255, 255, 255)) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(1,2,3)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3

