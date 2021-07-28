T = int(input())

for timecase in range(T):
    n,m = map(int,input().split())
    size = [list(map(int, input().split())) for _ in range(n)]
    
    max = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            attack = 0
            for k in range(m):
                for l in range(m):
                   attack += size[j+l][i+k]
                if attack > max:
                    max = attack
    print("#{} {}".format(timecase+1,max))
