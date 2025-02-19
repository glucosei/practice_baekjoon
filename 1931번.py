N = int(input())
List = [tuple(map(int, input().split())) for _ in range(N)]

# 회의의 종료 시간을 기준으로 정렬
List = sorted(List, key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for meeting in List:
    if meeting[0] >= end_time:
        cnt += 1
        end_time = meeting[1]

print(cnt)