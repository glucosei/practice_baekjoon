from copy import deepcopy
def simulate(box):
    if all(all(x == 1 for x in row) for row in box):
        return 0
    elif all(all(x == 0 for x in row) for row in box):
        return -1
    cnt = 0
    while True:
        before = deepcopy(box)
        cnt += 1
        for i in range(len(box)):
            for j in range(len(box[0])):
                if box[i][j] == 1:
                    if i > 0 and box[i-1][j] == 0:
                        box[i-1][j] = 1
                    if i < len(box)-1 and box[i+1][j] == 0:
                        box[i+1][j] = 1
                    if j > 0 and box[i][j-1] == 0:
                        box[i][j-1] = 1
                    if j < len(box[0])-1 and box[i][j+1] == 0:
                        box[i][j+1] = 1
        if before == box:
            return -1
        if all(all(x == 1 for x in row) for row in box):
            return cnt




N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]

print(simulate(box))