import string

def is_pangram(s):
    print(set(s.lower()))
    print(set(string.lowercase))
    return set(string.lowercase) <= set(s.lower())

is_pangram( "The quick brown fox jumps over the lazy dog" )