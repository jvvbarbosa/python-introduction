# python-introduction
All the slides for the course can be found in

https://jgcourses.gitlab.io/python-introduction/


lambda a,b : a+b

The functions which takes (arguments) a and b, and returns (result) a + b


\**Division for python 2**
python 2 truncates 3/2 to 1 while python 3 does not and gives 1.5

\**Ways of looking at exceptions:**
1) Messages from top of stack to anyone who cares lower down

2) Branching mechanism

3) Qualitatively different answer to some question

4) Alternative channel for information flow out of functions




\** Unit testing **

module unittest

or (far better) pytest



\** for performance enhacement look for Cython or Numba **

Cython converts stuff into C 
Numba speeds up mathematical operations

Using Numba:

from numba import jit

@jit
def math_fn() #This now runs super fast



\** @property **

In a class putting 
@property
def fn(self)

makes is possible to call a function as if it were data 

Class bla()
...

a = bla()

bla.fn  #This is good
