import itertools
import string
"""
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
hexdigits = '0123456789abcdefABCDEF'
octdigits = '01234567'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace = ' \t\n\r\x0b\x0c'

Formula is [26] lowercase letter + [26] Uppercase = 52
52 power range of the password
"""
char=string.ascii_letters#type of chars in the password
r=3#range of password
x=0#number of possibilities
try:
        for i in itertools.product(char, repeat=r):
                x+=1
                #print('').join(i),x
        print(x)
except KeyboardInterrupt:
        print(x)
#print(x)#print final number of possibilities