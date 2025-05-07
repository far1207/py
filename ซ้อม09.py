x = str(input(" : "))
print(len(str(x)))
e = []
b = []
for i in x :
    e.append(i)
for j in e :
    k=int(j)
    if k%5==0 :
        b.append("X")
    else:
        b.append("*")
print("".join(map(str,b)))