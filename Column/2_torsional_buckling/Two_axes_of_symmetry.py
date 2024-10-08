import math

#material properties Kg/cm2
E = 2.04e+06
Fy = 3600
nu = 0.3
G = E/(2*(1+nu))

#section properties-cm^4
Ix = 2082 #cm^4
Iy = 2082 #cm^4

L = 500 #cm

J = 10.43 #cm^4
Cw = 26810 #cm^4

Kz = 1 #for safty it sets to 1

Fe = ( ( (math.pi**2*E*Cw)/((Kz*L)**2) ) + (G*J) )*(1/(Ix+Iy))

if Fy/Fe <= 2.25:
    Fcr = ( 0.658**(Fy/Fe) )*Fy
else:
    Fcr = 0.877*Fe

print(Fcr)