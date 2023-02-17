import numpy as np
L = 12 #Length of beam in meters
w = 10 #intensity of load in KN/m

 
#Question a
#Bending moment(M) and shear force(V) at the first end, x=0
x = 0
M = (w*(-6*x**2 + 6*L*x - L**2)/12)
V = w*(L/2 - x)
 
a = "The bending moment at x=0 is "
b = "the shear force at x=0 is "
print("a.1. "+a+str(M)+" and "+b+ str(V))

#Bending moment(M) and shear force(V) at the first end, x=L=10
x = L
M = (w*(-6*x**2 + 6*L*x - L**2)/12)
V = w*(L/2 - x)

a = "The bending moment at x=L is "
b = "the shear force at x=L is "
print("a.2. "+a+str(M)+" and "+b+ str(V))

#Question b
print()
print("b.1. When the bending moment is zero, we get an expression x**2 - Lx + (L**2)/6 =0") 
#from the expression
a = 1
b = -L
c = (L**2)/6

discriminant = b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a

print("b.2. The points of contraflexure are "+str(root_1b)+" and "+str(root_2b))

#Question c
#When shear force is zero, we get an expression L - 2*x = 0 
#but 
x = L/2 
L = 12

print()
print("c. The point at which the shear force will be zero is "+str(x))


#Question d
x = np.arange(0,L + 0.01, 0.01) #0.01 represents the 10mm converted to metres
M = (w*(-6*x**2 + 6*L*x - L**2)/12)

print()
print("d. Using the initialized variable, the bending moment at each 10mm step across the 12m span in the array is "+str(M))

#Question e
V = w*(L/2 - x)

print()
print("e. The shear force for each step along the span is "+str(V))

#Question f
#let absolute value of the bending moment array be H
#Let minimum absolute value of the bending moment array be h
H = abs(M)
h = min(H)

#If bending moment is h, x**2 - Lx + (L**2)/6 + (2*h)/w = 0
#from the expression
a = 1
b = -L
c = (L**2)/6 + (2*h)/w

#Using the Almighty formular the roots are:
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a

print()
print("f. The points along L at which the absolute values of the bending moment array is minimum are "+str(root_1f)+" and "+str(root_2f))

#Question g
#let relative errors be r_e

r_e1 = ((root_1b - root_1f)/root_1b*100)
r_e2 = ((root_2f - root_2b)/root_2f*100)

print()
print("g. The relative errors between estimated points of contraflexure are "+str(r_e1)+" and "+str(r_e2))

#question h
#let maximum bending moment be M_max and minimum bending moment be M_min
#for the maximum
M_max = max(M)

#When the bending moment is M_max, we get an expression x**2 - Lx + (L**2)/6 + (2*M_max)/w = 0
a = 1
b = -L
c = (L**2)/6 + (2*M_max)/w

#Using the almighty formular:
discriminant = b**2 - 4*a*c
root_1h = (-b + np.sqrt(discriminant))/2*a
root_2h = (-b - np.sqrt(discriminant))/2*a

print()
print("h.1. The points at which bending moment is maximum occurs at {0} and {1}".format(root_1h,root_2h))

#for the minimum
M_min = min(M)
#When the bending moment is M_max, we get an expression x**2 - Lx + (L**2)/6 + (2*M_min)/w = 0
a = 1
b = -L
c = (L**2)/6 + (2*M_min)/w

#Using the almighty formular:
discriminant = b**2 - 4*a*c
root_1i = (-b + np.sqrt(discriminant))/2*a
root_2i = (-b - np.sqrt(discriminant))/2*a

print()
print("h.2. The points at which the minimum bending moment occurs are {0} and {1}".format(root_1i,root_2i))

#GitHub link = https://github.com/Fredmann099/Computer-Application-Assignment-3.git


