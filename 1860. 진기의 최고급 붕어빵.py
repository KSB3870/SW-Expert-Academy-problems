T = int(input())

for timecase in range(T):
    n,m,k = map(int,input().split())
    customer = list(map(int,input().split()))
    customer.sort()
    answer = "Possible"
    for i in range(n):
        fish = (customer[i] // m) * k
        if fish < i+1:
            answer =  "Impossible"
    print("#{} {}".format(timecase+1,answer))

