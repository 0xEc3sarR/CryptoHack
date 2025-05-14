# given string 'label' and integer 13
from Crypto.Util.number import bytes_to_long
from pwn import *

string = 'label'

print("crypto{", end='')
for i in range(len(string)):
    #print(ord(string[i]), end=' ')
    a = ord(string[i])
    xor_operation = a ^ 13
    print(chr(xor_operation), end='')

print("}")


