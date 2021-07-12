import random
import statistics

def random_list(size):
    result = []

    for n in range(size):
        result.append(random.randint(9,199))

    return result

n=int(input())
result = random_list(n)
result.sort()
print(result)
print(statistics.median(result))
