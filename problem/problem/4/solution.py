from collections import Counter

def solution(s):
    s = list(s)
    occurence_number = Counter(s)
    most_common_number = int(occurence_number.most_common(1)[0][0])
    return most_common_number