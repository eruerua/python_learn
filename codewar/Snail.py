def snail_sort(n):
    if n==1:
        return [1]
    if n==2:
        return [1,2,4,3]
    l=list(range(1,n+1))
    l+=[n*i for i in range(2,n+1)]
    l+=[n**2-i for i in range(1,n-1+1)]
    l+=[n**2-(n-1)-n*i for i in range(1,n-2+1)]
    m_l=sorted(set(range(1,n**2+1))-set(l))
    print(l,m_l)
    l+=[m_l[i-1] for i in snail_sort(n-2)]
    return l

def snail(snail_map):
    print(snail_map)
    if snail_map==[[]]:
        return []
    n=len(snail_map)
    flat_l=[y for x in snail_map for y in x]
    order_list=snail_sort(n)
    print(order_list)
    l=[]
    for i in order_list:
        l.append(flat_l[i-1])
    return l
array=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
print(snail(array))