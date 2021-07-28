T = int(input())

for timecase in range(T):
    case_num = input()
    grade_list = [0]*101
    max = 0
    grade = 0
    num_list = list(map(int,input().split()))
    for i in range(len(num_list)):
        grade_list[num_list[i]] += 1
    for j in range(1,len(grade_list)):
        if max <= grade_list[j]:
            max = grade_list[j]
            grade = j

    print('#{} {}'.format(timecase+1,grade))
    
