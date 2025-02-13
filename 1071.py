#1071: 소트

K = int(input())
List = list(map(int, input().split(" ")))

def switch(A,B):
    return B,A
#위반 부분 검사
while True:
    run = 0
    for i in range(K-2, -1, -1):
        if List[i+1] - List[i] == 1:
            List[i],List[i+1] = switch(List[i],List[i+1])
            run = 1
            break
    if run == 0:
        break
for i in range(K):
    print(List[i], end = ' ')