print("Area and Volume Calculator")
print("")
print("Circle = 1")
print("Chemistry Square = 2")
print("Rectangle = 3")
print("Triangle = 4")
print("")
circle=1
cs=2
ra=3
ta=4
a=int(input("What is your choice : " ))
if a==1:
    print("")
    print("Area of Circle")
    print("")
    r=float(input("Radius : "))
    print("")
    pi=22/7
    sperimeters=2*(22/7)*r
    area=pi*(r**2)
    print("Perimeters = ", sperimeters)
    print("Area = ",area )
if a==2:
    print("")
    print("Perimeter and Area of Chemistry Square")
    print("")
    los=float(input("Length of Side : "))
    sqperimeters=los*4
    sqarea=los**2
    print("Perimeters = ", sqperimeters)
    print("Area = ",sqarea)
if a==3:
    print("")
    print("Perimeters and Area of Rectangle")
    print("")
    rlength=float(input("Length : "))
    rwidth=float(input("Width : "))
    rperimeters=(2*rwidth)+(2*rlength)
    rarea=rwidth*rlength
    print("")
    print("Perimeters = ",rperimeters)
    print("Area = ",rarea)
if a==4:
    print("")
    print("Area of Triangle")
    print("")
    b=float(input("Base : "))
    th=float(input("Height : "))
    tarea=1/2*b*th
    print("")
    print("Area = ",tarea)
    print("Do you want to calculate perimeters?")
    print("Yes=1")
    print("No=0")
    print("")
    tps=int(input("1 or 0 : "))
    if tps==1:
        print("")
        print("Perimeters of Triangle")
        print("")
        print("Input lengths below ")
        print("")
        tp1=float(input("Length 01 : "))
        tp2=float(input("Length 02 : "))
        tp3=float(input("Length 03 : "))
        tp=tp1+tp2+tp3
        print("Perimeters = ",tp)
    else:
        print("Thank You")





print("")
input("Enter for exit")



