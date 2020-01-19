def primeFactors(n):
    l=[]
    while n > 1:
        for i in range(2,n+1):
            if n % i ==0:
                l.append(i)
                break
        n=n//i
    s=''
    for i in sorted(set(l)):
        a=l.count(i)
        if a==1:
            s+='({})'.format(i)
        else:
            s+='({}**{})'.format(i,a)
    return s
print(primeFactors(7775460))
