t=int(input())
cnt=0
if  t>=1 and t<=20000:
    while t>0:
        a,b=map(int,input().split())
        if a>=1 and b>=1 and a<1000000000 and b<=1000000000:
            d=abs(a-b)
            if d!=0:
                while d>=10:
                    cnt+=1
                    d-=10
                cnt+=1
            print(cnt)
        t-=1
