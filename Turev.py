import sympy as sym
import math
x=sym.symbols("x" )
y=sym.symbols("y")

xx= sym.diff((sym.diff(((1-x)**2+ 100*(y-x**2)**2),x)),x)
xy =sym.diff((sym.diff(((1-x)**2+ 100*(y-x**2)**2),x)),y)

yx = sym.diff((sym.diff(((1-x)**2+ 100*(y-x**2)**2),y)),x)
yy = sym.diff((sym.diff(((1-x)**2+ 100*(y-x**2)**2),y)),y)


hessian=[[xx,xy],[yx,yy]]
print(hessian)


y=sym.Symbol("x")
print(sym.diff(x*(5*3.14-x),y))



# (1-x1)^2+ 100(x2-x1^2)^2

#(1-2r)^2 + 100(0-4r^2)^2

#Gutter oluk problemi

