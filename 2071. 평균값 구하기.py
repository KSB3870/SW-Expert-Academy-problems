T = int(input())
for timecase in range(T) :
    nums = list(map(int,input().split()))
    average = (sum(n for n in nums)/len(nums))
    avg = int(round(average))
    print( f"#{timecase+1} {avg}" )
