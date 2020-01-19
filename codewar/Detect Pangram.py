import string

def is_pangram(s):
    l=list(set([i.lower() for i in s if i.isalpha()]))
    l.sort()
    s=''.join(l)
    if s==string.ascii_lowercase:
        return True
    else:
        return False

print(is_pangram( "The quick brown fox jumps over the lazy dog" ))