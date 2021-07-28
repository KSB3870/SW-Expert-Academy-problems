T = int(input())
for timecase in range(T):
    sdocu_map = [list(map(int, input().split())) for _ in range(9)]
    num_list = set([1,2,3,4,5,6,7,8,9])
    result = 1

    for garo in range(9):
        if set(sdocu_map[garo]) != num_list:
            result = 0;
            break
    else:
        for sero in range(9):
            temp = set()
            for garo in range(9):
                temp.add(sdocu_map[garo][sero])
            if temp != num_list:
                result = 0
                break
        else:
            for garo in range(0,9,3):
                if not result:
                    break
                else:
                    for sero in range(0,9,3):
                        temp = set()
                        for square_garo in range(3):
                            for square_sero in range(3):
                                temp.add(sdocu_map[garo + square_garo][sero + square_sero])
                        if temp != num_list:
                            result = 0
                            break
    print("#{} {}".format(timecase+1, result))
