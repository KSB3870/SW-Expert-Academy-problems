T = int(input())
for timecase in range(T) :
    nums = map(int,input().split())
    res = sum(n for n in nums if n%2==1)
    print( f"#{timecase+1} {res}" )
