T = int(input())
for timecase in range(1,T+1):
    case = int(input())
    money = list(map(int, input().split()))
    last = money[-1]
    get = 0
    for i in range(len(money)-1,-1,-1):
        if last>money[i]:
            get += last - money[i]
        else:
            last = money[i]
    print("#{} {}".format(timecase,get))
