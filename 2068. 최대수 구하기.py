T = int(input())
for timecase in range(T) :
    nums = list(map(int,input().split()))
    max_num = max(nums)
    print( f"#{timecase+1} {max_num}" )
