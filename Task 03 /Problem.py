def primefac(n):
    i=2
    while i**2<=n:
        if n%i:
            i+=1
        else:
            n//=i
    return n

l1=[]
t = int(input(""))
for i in range(t):
    r=primefac(int(input("")))
    l1.append(r)
for i in l1:
    print(i)
    
