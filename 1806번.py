def twoPointer(N, S, List):
    left = 0
    right = 0
    best = float('inf')
    current_sum = 0

    while True:
        if current_sum >= S:
            best = min(best, right - left)
            current_sum -= List[left]
            left += 1
        elif right == N:
            break
        else:
            current_sum += List[right]
            right += 1

    return best if best != float('inf') else 0

N, S = map(int, input().split())
List = list(map(int, input().split()))

print(twoPointer(N, S, List))