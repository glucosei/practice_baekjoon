#11003: 최솟값 찾기

N, L = map(int, input().split(" "))
List = list(map(int, input().split(" ")))
minList = []

for end in range(1, N+1):
    start = end-L+1
    if start<=0:
        start = 1
    if len(minList) == 0:
        minList.append(min(List[start-1:end]))
    else:
        minList.append(min(minList[end-2], List[end-1]))
    
for i in range(N):
    print(minList[i],end = " ")