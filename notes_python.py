c1 = complex(2, 2)

cc = c1.conjugate #bound method
cc() #can be called without the arguments

d = complex.conjugate #unbound method
d(c1) #needs to be called with argument

c1.real
c1.imag
c1.conjugate()


#Importing modules
#import math
#import math, cmath
#import math as calc #(then call calc.sin instead of math.sin)
#from math import sin #(can call sin() directly)
#from math import * #(can call anything inside math directly as above, but might cause name clashes, so it is unadvised)


#try calling dir() after each one of these commands on a fresh python env


#Lists, tuples and strings 

#careful with passing tuples into functions
b=1, #this is a tuple of 1 element, comma is essential to distinguish from the integer (1)
a=1,2
type(a) #this works

type(1,2) #does not work because now we are passing 2 arguments
type((1,2)) #This works as well

#Tuples cannot be modified once created, they are IMMUTABLE, whereas lists are MUTABLE

#Operations on lists and tuples

l1 = [1, 2, 3]
l2 = l1
l2 == l1 ,l2 is l1
l2 += [4, 5]
l1, l2
l1 == l2 , l2 is l1

t1 = (1, 2, 3)
t2 = t1
t2 == t1 ,t2 is t1
t2 += (4, 5)
t1, t2
t1 == t2 , t2 is t1

i1 = 0
i2 = i1
i2 == i1 ,i2 is i1
i2 += 1
i1, i2
i1 == i2 , i2 is i1


#Indexing and slicing 


a = list(range(10))
a[3]
a[-3]
a[3:6]
a[3:-3]
a[6:3]
a[:6]
a[0:6:2]
len(a)
a[2:4] = ['x']
a[-1:] = 'abc'


