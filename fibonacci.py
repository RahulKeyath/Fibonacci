n=int(input("Enter number:"))
a=1
for i in range(n):
    a*=n
    n-=1
print(a)
