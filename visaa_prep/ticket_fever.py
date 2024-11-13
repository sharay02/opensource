n=int(input())
for _ in range(n):
    s,t = map(int,input().split())
    m = max(0,s-t)
    print(m)
