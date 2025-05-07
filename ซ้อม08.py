z = []
a=b=c=d=e=f=g=h=i=j=0
n=0
while True :
    x = int(input("รับค่า : "))
    if x <0 or x >= 10 :
        break
    else :
      z.append(x)
for y in z :
    if y == 0 :
        a = a+1
    if y == 1 :
        b = b+1
    if y == 2 :
        c = c+1
    if y == 3 :
        d = d+1
    if y == 4 :
        e = e+1
    if y == 5 :
        f = f+1
    if y == 6 :
        g = g+1
    if y == 7 :
        h = h+1
    if y == 8 :
        i = i+1
    if y == 9 :
        j = j+1
m = [a,b,c,d,e,f,g,h,i,j]
for v in m :
    print(n,"=",v)
    n=n+1