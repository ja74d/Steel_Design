import math

#kg/cm^2
Fy = 2400
E = 2.04e+06

#Calculating lambda all length are in "cm"
kx = 1.448
ky = 1
l = 400

#Section Properties
rx = 10.3
ry = 6.08

#lambda
landax = (kx*l)/rx
landay = (ky*l)/ry

landa = max(landax, landay)

Fe = ((math.pi)**2 * E)/(landa**2)

if Fy/Fe <= 2.25:
    Fcr = ( 0.658**(Fy/Fe) )*Fy
else:
    Fcr = 0.877*Fe

print(Fcr)
