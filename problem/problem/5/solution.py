def solution(S):

    N = 0 # 연산 횟수
    num = int(S, 2)

    while not num == 0:
        if num%2 == 0:
            num /= 2
        else:
            num -= 1

        N += 1
    return N