n=int(input())
sum=0
while n!=0:
    last_digit=n%10
    sum=sum+last_digit
    n//=10
print(sum)
