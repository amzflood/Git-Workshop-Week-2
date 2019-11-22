#fibonnaci

a = 1
b = 1
n = 1000
while(n-2):
    c = a + b
    a = b
    b = c
    print(c)
    n = n - 1
