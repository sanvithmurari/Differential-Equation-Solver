def exact_sol(M,N): 
    iM=sp.simplify(sp.integrate(M,x))
    g_prime=sp.simplify(N-sp.simplify(sp.diff(iM,y)))
    iN=sp.simplify(sp.integrate(g_prime,y))
    print('The general solution is: ')
    print(iM, " + ", iN, "= c")

def is_homogenous(M,N):
    t=sp.symbols('t')
    ratioM=sp.simplify(M.subs({x: t*x, y: t*y}) / M)
    ratioN=sp.simplify(N.subs({x: t*x, y: t*y}) / N)
    degree=sp.simplify(ratioN-ratioM)
    if(not(ratioM.has(x)) and not(ratioM.has(y))):
        if(degree==0 and not(ratioN.has(x)) and not(ratioN.has(y))):
            print("The equation is homogenous")
            return True

import sympy as sp
x,y=sp.symbols('x y')
print("*********************************")
print("EXACT DFFERENTIAL EQUATION SOLVER")
print("*********************************")
print("Enter equation of the form 'Mdx + Ndy=0'")
m=input("Enter M: ")
n=input('Enter N: ')
M=sp.sympify(m)
N=sp.sympify(n)
print("The differential equation is (",M,")dx + (",N,")dy = 0\n")
dMdy=sp.diff(M,y)
dNdX=sp.diff(N,x)
if(sp.simplify(dMdy-dNdX)==0):
    print("The Differential Equation is Exact\n")
    exact_sol(M,N)
else:
    print("The differential equation is not exact")

    #TYPE-1
    if(is_homogenous(M,N)):
        IF=sp.simplify(1/(M*x+N*y))
        M_prime=M*IF
        N_prime=N*IF
        if(sp.simplify(sp.diff(M_prime,y)-sp.diff(N_prime,x))==0):
            exact_sol(M_prime,N_prime)