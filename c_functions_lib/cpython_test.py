from ctypes import *

so_file = "/Users/flagada/Desktop/codecademy-learnPython/c_functions.so"
c_functions = CDLL(so_file)

print(type(c_functions))


test_int = c_functions.return_int(5, 5)
print(test_int)

c_functions.print() 

message = 'Hello'
message = list(message)
int_char = ord(message[0])
message[0] = chr(c_functions.test_char(ord(message[0])))
print(message)

print(len("HEllo"))
c_functions.print_str("Hello", 5)
c_functions.print_test("Hello")
