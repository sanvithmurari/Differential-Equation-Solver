def exact_sol(M,N): 
    iM=sp.simplify(sp.integrate(M,x))
    g_prime=sp.simplify(N-sp.simplify(sp.diff(iM,y)))
    iN=sp.simplify(sp.integrate(g_prime,y))
    print('The general solution is: ')
    sol=sp.simplify(iM+iN)
    print(sol, "= c")

def non_exact_sol(M,N,IF):
    print("Attempting to find an integrating factor...")
    print("Integrating factor is: ", IF)
    M_prime=M*IF
    N_prime=N*IF
    if(sp.simplify(sp.diff(M_prime,y)-sp.diff(N_prime,x))==0):
        exact_sol(M_prime,N_prime)

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
print("The differential equation is (",M,")dx + (",N,")dy = 0")
dMdy=sp.diff(M,y)
dNdx=sp.diff(N,x)
if(sp.simplify(dMdy-dNdx)==0):
    print("The Differential Equation is Exact")
    exact_sol(M,N)
else:
    print("The differential equation is not exact")
    #TYPE-1
    if(is_homogenous(M,N)):
        IF=sp.simplify(1/(M*x+N*y))
        non_exact_sol(M,N,IF)
    
    #TYPE-2
    u=sp.symbols('u')
    A,B=sp.simplify(M/y),sp.simplify(N/x)
    A=A.subs({x*y: u})
    B=B.subs({x*y: u})
    if(not(A.has(x)) and not(A.has(y)) and not(B.has(x)) and not(B.has(y))):
        IF=sp.simplify(1/(M*x-N*y))
        non_exact_sol(M,N,IF)
    
    #TYPE-3
    check=sp.simplify((dNdx-dMdy)/M)
    if(not(check.has(x))):
        IF=sp.simplify(sp.exp(sp.integrate(check,y)))
        non_exact_sol(M,N,IF)
    
    #TYPE-4
    check=sp.simplify((dMdy-dNdx)/N)   
    if(not(check.has(y))):
        IF=sp.simplify(sp.exp(sp.integrate(check,x)))
        non_exact_sol(M,N,IF)
    