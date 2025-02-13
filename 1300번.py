import math

def get_divisors_count(n, N):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i <= N:
                count += 1
            if i != n // i and n // i <= N:
                count += 1
    return count

N = int(input())

# 필요한 값만 계산하여 저장
List = []
for i in range(1, N**2 + 1):
    count = get_divisors_count(i, N)
    if count > 0:
        List.append((i, count))

k = int(input())

# 이진 탐색을 사용하여 k번째 값을 찾기
left, right = 0, len(List) - 1
while left <= right:
    mid = (left + right) // 2
    total = sum(count for _, count in List[:mid + 1])
    if total < k:
        left = mid + 1
    else:
        right = mid - 1

# k번째 값을 찾기 위해 다시 합산
total = 0
for value, count in List:
    total += count
    if total >= k:
        print(value)
        break