import math

#symmetric to
S = 1 #1=x or 2=y

#material properties Kg/cm2
E = 2.04e+06
Fy = 3600
nu = 0.3
G = E/(2*(1+nu))

#Section properties
L = 350 #cm
Ix = 1910 #cm^4
Iy = 148 #cm^4
A = 32.2 #cm^2
y0 = 3.94 #cm it is defined as Xm in eourucode
rx = 7.7 #cm
ry = 2.14 #cm
kx = 1
ky = 1
kz = 1
Cw = 9065 #cm^2
J = 12.3 #cm^2

lambdax = kx*L/rx
lambday = ky*L/ry

r0 = (Ix+Iy)/A + y0**2
r0 = r0**0.5

Fex = ((math.pi**2)*(E))/(lambdax**2)
Fey = ((math.pi**2)*(E))/(lambday**2)
Fez = ( ( (math.pi**2*E*Cw)/(kz*L)**2 ) + ( G*J ) )*( 1/(A*r0**2) )
H = 1-( (y0**2)/(r0**2) )


if S==0:
    Fe = ( (Fey+Fez)/(2*H) )*( 1 - ( 1 - ( (4*Fex*Fez*H)/((Fex+Fez)**2) ) )**0.5 )
elif S==1:
    Fe = ( (Fey+Fez)/(2*H) )*( 1 - ( 1 - ( (4*Fey*Fez*H)/((Fey+Fez)**2) ) )**0.5 )

#calculation of Fcr
if Fy/Fe <= 2.25:
    Fcr = ( 0.658**(Fy/Fe) )*Fy
else:
    Fcr = 0.877*Fe

print(Fcr)