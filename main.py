import math as m
from math import degrees


def uhol_alpha(a,b,c):
    cos_alpha = (-a**2+b**2+c**2)/(2*b*c)
    alpha_radian = m.acos(cos_alpha)
    alpha = m.degrees(alpha_radian)
    return alpha

def uhol_beta(a,b,c):
    beta = m.degrees(m.acos((-b**2+a**2+c**2)/(2*a*c)))
    return beta

def uhol_gamma(a,b,c):
    gamma = m.degrees(m.acos((-c**2+a**2+b**2)/(2*a*b)))
    return gamma

print(uhol_gamma(6,5,8))
print(uhol_beta(6,5,8))

