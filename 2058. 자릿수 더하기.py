def sum_digit(number):
    num = str(number)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum
num = int(input())
print("{}".format(sum_digit(num)))
