import sys
import copy
from collections import deque

def move(board, direction):
    N = len(board)
    new_board = [[0] * N for _ in range(N)]
    
    for i in range(N):
        # 한 줄씩 압축을 수행할 리스트 (0을 제외하고 담음)
        line = deque()
        
        if direction == 0:  # 위로 이동
            for j in range(N):
                if board[j][i] != 0:
                    line.append(board[j][i])
        elif direction == 1:  # 아래로 이동
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    line.append(board[j][i])
        elif direction == 2:  # 왼쪽으로 이동
            for j in range(N):
                if board[i][j] != 0:
                    line.append(board[i][j])
        else:  # 오른쪽으로 이동
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    line.append(board[i][j])

        # 블록 합치기 (큐를 사용하여 2개씩 확인)
        new_line = deque()
        while line:
            if len(line) >= 2 and line[0] == line[1]:  # 같은 블록이면 합침
                new_line.append(line.popleft() * 2)
                line.popleft()  # 두 번째 블록 제거
            else:
                new_line.append(line.popleft())

        # 새로운 보드에 저장 (빈 공간은 0으로 채움)
        while len(new_line) < N:
            new_line.append(0)

        for j in range(N):
            if direction == 0:  # 위
                new_board[j][i] = new_line[j]
            elif direction == 1:  # 아래
                new_board[N-1-j][i] = new_line[j]
            elif direction == 2:  # 왼쪽
                new_board[i][j] = new_line[j]
            else:  # 오른쪽
                new_board[i][N-1-j] = new_line[j]

    return new_board

def dfs(depth, board):
    global max_block

    # 최대 블록 값 갱신
    max_block = max(max_block, max(map(max, board)))

    # 5번 이동까지 모두 탐색
    if depth == 5:
        return

    for direction in range(4):
        new_board = move(copy.deepcopy(board), direction)
        dfs(depth + 1, new_board)

# 입력 처리
N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 최대 블록 값 초기화
max_block = 0
dfs(0, board)

# 결과 출력
print(max_block)
