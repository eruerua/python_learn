def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        print(a)
        array = list(zip(*array))
        print(array)
        array.reverse()
        print(array)
    return a

snail([[1,2,3],
       [4,5,6],
       [7,8,9]])