import sys

def solution(A):
    max_profit = 0 # 최대수익
    min_price = sys.maxsize # 저점

    # 반복을 통해 고점과 저점을 갱신
    for price in A:
        min_price = min(min_price, price)
        max_profit = max(price - min_price, max_profit)

    return max_profit