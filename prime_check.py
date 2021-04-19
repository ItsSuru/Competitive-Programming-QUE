n=int(input())
i=2
prime=0
while i<n:
    if n%i==0:
        prime=1
        break
    i+=1
if prime==0:
    print("yes")
else:
    print("no")
