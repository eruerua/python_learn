def is_valid_IP(strng):
    l=strng.split('.')
    if len(l)!=4:
        return False
    else:
        for i in l:
            if len(i)>=2 and i[0]=='0':
                return False
            if not (i.isdigit()) or int(i)>255 or int(i)<0  :
                return False
        return True
