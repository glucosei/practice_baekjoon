from itertools import combinations
from bisect import bisect_left, bisect_right

def get_subsums(arr):
    subsums = []
    n = len(arr)
    for i in range(n + 1):
        for comb in combinations(arr, i):
            subsums.append(sum(comb))
    return subsums

def count_sums(S, left, right):
    left_sums = get_subsums(left)
    right_sums = get_subsums(right)
    
    left_sums.sort()
    count = 0

    for r in right_sums:
        target = S - r
        count += bisect_right(left_sums, target) - bisect_left(left_sums, target)

    return count - (1 if S == 0 else 0)

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = nums[:N//2], nums[N//2:]
print(count_sums(S, left, right))
