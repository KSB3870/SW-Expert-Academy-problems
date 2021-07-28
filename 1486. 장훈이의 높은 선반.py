T = int(input())

def top(index, height):
    global max_height
    if b <= height < max_height:
        max_height = height
    if index == n:
        return
    top(index+1, height)
    top(index+1, height+s[index])

for timecase in range(T):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    max_height = 200000
    top(0,0)
    print ('#{} {}'.format(timecase+1, max_height - b))

