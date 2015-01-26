__author__ = 'Sumanesh Magarabooshanam'

def reset(b):
    print("Before reset : {0}".format(b))
    b[:] = [0, 1, 2, 3, 4, 5]
    print("After reset : {0}".format(b))

############################################################################################################

#type(obj) - Determines type of the object
i = 10
print ("i with value {0} is of type {1}".format(i,type(i)))

#isinstanceof - to check whether the object supports this type
print(" i isinstanceof int : {0}".format(isinstance(i, float)))

############################################################################################################

# a real long number
h = 123456789012345678901234567890123456789012345678901234567890

print(h+5)

i = 1.2e0j
print("real : {0}, imag : {1}".format(i.real,i.imag))

############################################################################################################

listOfNumbers = [1, 20, 30, 4, 5]
print(1 in listOfNumbers)

print("listOfNumbers[0] : {0} ".format(listOfNumbers[0]))
print("listOfNumbers[-1] : {0}".format(listOfNumbers[-1]))
print(listOfNumbers[2:4])  # Lower bound is included but upper bound is not included

...
a = [0, 1, 2, 3, 4, 5]
a[1:2] = [10, 20, 30]
print(a)
reset(a)
print(a)
...