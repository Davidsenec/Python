def fac(x): 
    if x <= 1: return 1
    else:
        return x * fac(x-1)
    
n = int(input("Enter number: "))

for i in range(n):
    for j in range(n-i):
        print(end=" ")
    for j in range(i+1):
        print(fac(i)//(fac(j)*fac(i-j)), end=" ")
    
    print()
