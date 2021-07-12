T = int(input())
for timecase in range(T) :
    nums = list(map(int,input().split()))
    if nums[0] < nums[1]:
        print(f"#{timecase+1} <")
    elif nums[0] > nums[1]:
        print(f"#{timecase+1} >")
    else:
        print(f"#{timecase+1} =")
