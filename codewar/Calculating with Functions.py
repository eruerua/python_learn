
def zero(*args): #your code here
    if len(args)==0:
        return '0'
    else:
        return eval('0'+args[0])
def one(*args): #your code here
    if len(args)==0:
        return '1'
    else:
        return eval('1'+args[0])
def two(*args): #your code here
    if len(args)==0:
        return '2'
    else:
        return eval('2'+args[0])
def three(*args): #your code here
    if len(args)==0:
        return '3'
    else:
        return eval('3'+args[0])
def four(*args): #your code here
    if len(args)==0:
        return '4'
    else:
        return eval('4'+args[0])
def five(*args): #your code here
    if len(args)==0:
        return '5'
    else:
        return eval('5'+args[0])
def six(*args): #your code here
    if len(args)==0:
        return '6'
    else:
        return eval('6'+args[0])
def seven(*args): #your code here
    if len(args)==0:
        return '7'
    else:
        return eval('7'+args[0])
def eight(*args): #your code here
    if len(args)==0:
        return '8'
    else:
        return eval('8'+args[0])
def nine(*args): #your code here
    if len(args)==0:
        return '9'
    else:
        return eval('9'+args[0])

def plus(n): #your code here
    return '+'+n
def minus(n): #your code here
    return '-'+n
def times(n): #your code here
    return '*'+n
def divided_by(n): #your code here
    return '//'+n

print(seven(times(five())))