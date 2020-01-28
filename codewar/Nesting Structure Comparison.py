def printm(listin):
    a=[]
    if not isinstance(listin,list):
        return listin
    for i in listin:
        if isinstance(i,list):
            a.append(printm(i))
        else:
            a.append(1)
    return a
def same_structure_as(original,other):
    return printm(original)==printm(other)