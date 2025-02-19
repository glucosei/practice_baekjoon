import sys
import bisect

# 입력 받기
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# LIS 계산
lis = []  # LIS 배열
trace = [-1] * n  # LIS 구성 요소의 이전 인덱스 추적
index_list = [-1] * n  # LIS에 포함된 원소들의 실제 인덱스 저장

for i in range(n):
    pos = bisect.bisect_left(lis, arr[i])  # 이진 탐색을 통해 LIS 위치 찾기
    if pos == len(lis):
        lis.append(arr[i])  # LIS 끝에 추가
        index_list[pos] = i  # 실제 배열에서 LIS를 구성하는 인덱스 저장
    else:
        lis[pos] = arr[i]  # 기존 값을 대체
        index_list[pos] = i  # 인덱스 업데이트

    # 이전 LIS 원소의 인덱스를 저장하여 추적
    trace[i] = index_list[pos - 1] if pos > 0 else -1

# LIS 길이 출력
lis_length = len(lis)
print(lis_length)

# LIS 수열 복원
lis_seq = []
idx = index_list[lis_length - 1]  # LIS 마지막 원소의 인덱스
while idx != -1:
    lis_seq.append(arr[idx])
    idx = trace[idx]

# 역순으로 출력
print(*lis_seq[::-1])
