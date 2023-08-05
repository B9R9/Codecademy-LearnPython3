### C Functions Lib

***
## Introduction  
Discovering code possibility
***
## Objectives  
We can call a C function from Python program using the ctypes module.

## Installation  
I made the choice to centralize all these projects in a single repo.
This does not allow you to download c_functions_lib individually at the moment.
```
$ git clone git@github.com:B9R9/sandbox-Python3.git
$ cd ../path/to/the/folder/c_functions_lib
```
***
## Compilation
Step 1:
Creating a C file (.c extension) with the required functions.  
```
int square(int i){
  return (i * i);
}
```
Step 2:  
Creating a shared library file (.so extension) using the C compiler
```
$ cc -fPIC -shared -o my_functions.so my_functions.c
```
Step 3:  
In the Python program, create a ctypes.CDLL instance from the shared file.  
```
from ctypes import *
>>> so_file = "/Users/Path/To/my_functions.so"
>>> my_functions = CDLL(so_file)
>>> 
>>> print(type(my_functions))
<class 'ctypes.CDLL'>
>>> 
>>> print(my_functions.square(10))
100
>>> print(my_functions.square(8))
64
>>> 
```
***
Step 4:
Finally, call the C function using the format {CDLL_instance}.{function_name}({function_parameters}).
