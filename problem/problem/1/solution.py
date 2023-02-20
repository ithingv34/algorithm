def solution(n):
    # 누적합 구하기
    # S(n+1) = S(n) + n
    arr = [i for i in range(1, n)]

    return sum(arr) + n