t = int(input(""))
lst1=[]
def find(t):
    for i in range(t):
        sum1=0
        n = int(input(""))
        for j in range(n):
            if j%3==0 or j%5==0:
                sum1+=j
        lst1.append(sum1)
find(t)
for o in lst1:
    print(o)
        
