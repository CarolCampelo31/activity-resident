x = int(input())
y = int(input())
z = int(input())

if x >= y and x >= z:
    if y >= z:
        print (z)
        print (y)
        print (x)
    else:
        print (y)
        print (z)
        print (x)
        
elif y >= x and y >= z:
    if x >= z:
        print (z)
        print (x)
        print (y)
    else:
        print (x)
        print (z)
        print (y)
       
elif z >= x and z>= y:
    if x >= y:
        print (y)
        print (x)
        print (z)
    else:
        print (x)
        print (y)
        print (z)
print