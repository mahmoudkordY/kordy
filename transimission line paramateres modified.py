from cmath import *
L=float(input("enter the length of T.L :"))
R=float(input("enter the resistor :"))
X=float(input("enter the inductor reactance :"))
Y=float(input("enter the shunt admittance :"))
Y1=complex(0,Y)
z=complex(R,X)
methodtype=input("Enter the method type (approximate) or (exact) : ")
if methodtype == "approximate" and 0 <L <=80  :
    print("short model")
    model=input("enter the the model (shunt) or (series) :")
    if model == "series" :
               A = 1
               B = z 
               C = 0
    elif model == "shunt" :
             A = 1
             B = 0
             C = Y1
elif methodtype=="approximate" and L >80 and 0< L <= 160 :
    print("medium model")
    model=input("enter the the model(model pi or T) :")
    if model == "pi" :
               A = 1+(Y1*z)/2
               B = z 
               C = Y1*(1+(Y1*z)/4)
    elif model == "T" :
             A = 1+(Y1*z)/2
             B = z *(1+(Y1*z)/4) 
             C = Y1
elif methodtype == "exact" and L>0 :
            f=float(input("enter the frequency :"))
            Gamma= sqrt(z*Y1)
            Zc= sqrt(z/Y1)
            beta=Gamma.imag
            lamda=2*pi/beta
            phase_velocity=lamda * f
            print("wavlength = ",lamda)
            print("phase velocity = ",phase_velocity)
            exactmodel=input("enter model (exact pi) or exact model (exact T) or (hyberpolic model) : ")
            if exactmodel == "exact pi" :
                    zdash=Zc*sinh(Gamma)
                    ydash=Y1*tanh(Gamma/2)/(Gamma/2)
                    A = 1+(ydash*zdash)/2
                    B = zdash
                    C = ydash*(1+(ydash*zdash)/4)
            elif exactmodel == "exact T" :
                    zdash=Zc*tanh(Gamma/2)/(Gamma/2)
                    ydash=sinh(Gamma)/Zc
                    A = 1+(ydash*zdash)/2
                    B = zdash*(1+(ydash*zdash)/4)
                    C = ydash
            elif exactmodel == "hyberpolic model":
                    A = cosh(Gamma)
                    B = Zc*sinh(Gamma)
                    C =sinh(Gamma)/Zc
elif methodtype == "approximate" and L>160 :
        print("please enter valid length for approximate model where 0 < L < 160  ")
if L<0 :
        print("please enter valid length where L > 0 ")        
        print("Because the length can't be negative")
elif L>=0 :
        print("A = D = ",A)
        print("B = ",B)   
        print("C= ",C)
        ra=abs(A)
        theta_A = phase(A) * 180 / pi
        print(f"Polar form of A = D = {ra:.15f}∠{theta_A:.15f}°")
        rb=abs(B)
        theta_B = phase(B) * 180 / pi
        print(f"Polar form of B  = {rb:.15f}∠{theta_B:.15f}°")
        rc=abs(C)
        theta_C = phase(C) * 180 / pi
        print(f"Polar form of C  = {rc:.15f}∠{theta_C:.15f}°")
vrline=float(input("Enter the receiving end voltage (line) : "))
acpower=float(input("Enter the active power at the load : "))
powac=float(input("Enter the power factor at the load : "))
powac_type=(input("Enter the power factor type (leading) or (lagging) : "))
systemtype=(input("Enter the system type (1phase) or (3phase) : "))
if systemtype == "1phase":
        n=1
        vr=complex(vrline,0)
elif systemtype == "3phase":
        n=3
        vr=complex(vrline/sqrt(3),0)
if powac_type == "leading":
        Ir=complex(acpower/(n*vr),acpower*sqrt(1 - powac**2)/(n*vr*powac))
        x,u=polar(Ir)
        print("Ir = ",x,"∠",u*180/pi)
        vs=A*vr + B*Ir
        Is=C*vr + A*Ir
        k,angv=polar(vs)
        print("Vs = ",k,"∠",angv*180/pi)
        t,angi=polar(Is)
        print("Is = ",t,"∠",angi*180/pi)
        Ps=n*k*t*cos(angv - angi)
        print("Ps = ",Ps.real)
        eta=acpower*100/Ps.real
        print(f"efficiency  = {eta:.3f}%")
elif powac_type == "lagging":
        Ir=complex(acpower/(n*vr),-1*acpower*sqrt(1 - powac**2)/(n*vr*powac))
        x,u=polar(Ir)
        print("Ir = ",x,"∠",u*180/pi)
        vs=A*vr + B*Ir
        Is=C*vr + A*Ir
        k,angv=polar(vs)
        print("Vs = ",k,"∠",angv*180/pi)
        t,angi=polar(Is)
        print("Is = ",t,"∠",angi*180/pi)
        phiS=(angv-angi)
        Ps=3*k*t*cos(phiS)
        print("Ps = ",Ps.real)
        eta=acpower*100/Ps.real
        print(f"efficiency  = {eta:.3f}%")