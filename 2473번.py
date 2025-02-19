def find_closest_to_zero(arr):
    arr.sort()
    closest_sum = float('inf')
    closest_triplet = []

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1  # right 초기값을 len(arr) - 1로 수정
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if abs(current_sum) < abs(closest_sum):
                closest_sum = current_sum
                closest_triplet = [arr[i], arr[left], arr[right]]
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return closest_triplet

    return closest_triplet

N = int(input())
List = list(map(int, input().split()))
closest_triplet = find_closest_to_zero(List)

print(" ".join(map(str, sorted(closest_triplet))))
