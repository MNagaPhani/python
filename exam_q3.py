Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> m1=75
m2=87
m3=78
total=m1+m2+m3
print("Total marks obtained =",total)
avg=total/3
print("Average marks obtained =",avg)
if(90<=avg):
    print("A grade")
elif(80<=avg<90):
    print("B grade")
elif(70<=avg<80):
    print("C grade")
elif(60<=avg<70):
    print("D grade")
elif(50<=avg<60):
    print("E grade")
else:
    print("F grade")
