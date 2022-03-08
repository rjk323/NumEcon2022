import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# define global parameters

m = 0.5
phi = 0.3
e = 0.5
r = 0.03
t_g = 0.012
t_p = 0.04
p_bar = 3

# utility function
def ch_function(c,phi,h):
    u = c**(1-phi)*h**phi
    return u


#c onstraint 4
def tau_function(r,h,t_g,p_tilde,t_p, p_bar):
    tfo= r * h + t_g *p_tilde + t_p*max(p_tilde - p_bar, 0)
    return tfo

# constraint 3
def m_function(tfo,c):
    m = tfo + c
    return m

# constraint 2
def tilde_function(h,e):
    p_tilde = h * e
    return p_tilde

# Set up objective function:

def obj_function(m, phi, e, r,t_g,t_p,p_bar):
    c = cons(m, phi, e, r,t_g,t_p,p_bar)
    return -ch_function(c,phi,h)


# Use optimizer function to maximize (minimize the -u_function):

def opt(m, phi, e, r,t_g,t_p,p_bar):
    
    """ The function solves the consumer problem by optimizing utility
    
       Return the following: 
        c_star = optimal consumption
        h_star = optimal housing 
        u_star = utility given the housing and consumption
        result = prints the results """
    x_guess = (0,0)
    result = optimize.minimize(obj_function,x0=x_guess ,method='Nelder-Mead',args=(phi, e, r,t_g,t_p,p_bar))
    c_star = result.x
    h_star = cons(m, phi, e, r,t_g,t_p,p_bar)
    u_star = ch_function(c_star, phi,h_star)
    return [c_star, h_star, u_star]
                                      
c_star = opt(m, phi, e, r,t_g,t_p,p_bar)
h_star = opt(m, phi, e, r,t_g,t_p,p_bar)
u_star = opt(m, phi, e, r,t_g,t_p,p_bar)

# Define function that prints results:

def print_result(w, m, tau0, tau1, kappa, v, eps=0.3):
    print(f'Opitmal consumption is: {c_star:.3f}')
    print(f'Optimal housing is: {h_star:.3f}')
    print(f'Corresponding utility is: {u_star:.3f}')

# Print result