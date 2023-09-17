t = int(input().strip())
lst1 = []

def l(n):
    sum1 = 0
    x, y = 0, 1
    while x < n:
        lst1.append(x)
        x, y = y, x + y
    for j in lst1:
        if j % 2 == 0:
            sum1 += j
    return sum1

for i in range(t):
    n = int(input().strip())
    c = l(n)
    print(c)
