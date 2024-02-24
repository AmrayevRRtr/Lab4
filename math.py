ex1
import math
pi = math.pi
x = int(input("Input degree: "))
def degree_to_rad(x):
    res = x*pi/180
    return res
print("Output radian:", degree_to_rad(x))
ex2
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
area = (b1+b2)/2*h
print("Expected output:", area)
ex3
import math
num_of_sides = int(input("Input number of sides: "))
len_of_side = int(input("Input the length of a side: "))
tan = math.tan
apothem = len_of_side/2*math.tan(math.pi/num_of_sides)
area = num_of_sides*len_of_side*apothem/2
print("The area of polygon is:",area)
ex4
l = int(input("length_of_base: "))
h = int(input("Height of parallelogram: "))
def result(l, h):
    area = float(l*h)
    return area
print("Expected output:", result(l,h))