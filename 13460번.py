





def move(board, direction):
    N = len(board)
    M = len(board[0])

    def move_one_step(x, y, dx, dy):
        """공을 한 방향으로 끝까지 이동시키는 함수"""
        while True:
            nx, ny = x + dx, y + dy
            if board[nx][ny] == '#':  # 벽에 부딪히면 멈춤
                break
            if board[nx][ny] == 'O':  # 구멍에 빠지면 이동 종료
                return nx, ny
            x, y = nx, ny  # 계속 이동
        return x, y

    def move_ball(board, dx, dy):
        """공을 움직이고, R과 B가 겹치는 경우를 체크하는 함수"""
        new_board = [list(row) for row in board]
        red_pos, blue_pos = None, None
        red_in_hole, blue_in_hole = False, False

        # R, B의 초기 위치 찾기
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'R':
                    red_pos = (i, j)
                elif board[i][j] == 'B':
                    blue_pos = (i, j)

        # 이동 순서를 결정
        move_order = []
        if dx == -1:  # 위로 이동할 경우 위쪽에 있는 공부터
            move_order = sorted([red_pos, blue_pos], key=lambda x: x[0])
        elif dx == 1:  # 아래로 이동할 경우 아래쪽에 있는 공부터
            move_order = sorted([red_pos, blue_pos], key=lambda x: -x[0])
        elif dy == -1:  # 왼쪽 이동은 왼쪽에 있는 공부터
            move_order = sorted([red_pos, blue_pos], key=lambda x: x[1])
        elif dy == 1:  # 오른쪽 이동은 오른쪽에 있는 공부터
            move_order = sorted([red_pos, blue_pos], key=lambda x: -x[1])

        # 각 공을 차례로 이동
        for (x, y) in move_order:
            if (x, y) == red_pos:  # 빨간 공 이동
                new_x, new_y = move_one_step(x, y, dx, dy)
                if board[new_x][new_y] == 'O':
                    red_in_hole = True
                new_board[x][y] = '.'  # 기존 위치 비우기
                if not red_in_hole:
                    new_board[new_x][new_y] = 'R'
                red_pos = (new_x, new_y)

            elif (x, y) == blue_pos:  # 파란 공 이동
                new_x, new_y = move_one_step(x, y, dx, dy)
                if board[new_x][new_y] == 'O':
                    blue_in_hole = True
                new_board[x][y] = '.'  # 기존 위치 비우기
                if not blue_in_hole:
                    new_board[new_x][new_y] = 'B'
                blue_pos = (new_x, new_y)

        # 실패 조건: 파란 공이 구멍에 빠진 경우
        if blue_in_hole:
            return None

        # 성공 조건: 빨간 공만 구멍에 빠진 경우
        if red_in_hole:
            new_board[0][0] = '1'  # 종료 상태 반환

        # 실패 조건: 빨간 공과 파란 공이 같은 위치에 있는 경우
        if red_pos == blue_pos:
            return None

        return new_board

    # 방향 변환
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    dx, dy = directions[direction]
    return move_ball(board, dx, dy)


def print_board(board):
    """보드를 출력하는 함수"""
    if board is None:
        print("Failure: R and B met or B fell into the hole")
    else:
        for row in board:
            print(''.join(row))




"""
class QuaternaryTreeNode:
    def __init__(self, value, level):
        self.value = value
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.level = level

    def insert_child1(self, value):
        self.child1 = QuaternaryTreeNode(value)
        return self.child1

    def insert_child2(self, value):
        self.child2 = QuaternaryTreeNode(value)
        return self.child2

    def insert_child3(self, value):
        self.child3 = QuaternaryTreeNode(value)
        return self.child3

    def insert_child4(self, value):
        self.child4 = QuaternaryTreeNode(value)
        return self.child4

    
    def get_children_values(self):
        return [
            child.value if child else None
            for child in [self.child1, self.child2, self.child3, self.child4]
        ]

    def insert_auto(self, value):
        if self.child1 is None:
            self.child1 = QuaternaryTreeNode(value)
            return self.child1
        elif self.child2 is None:
            self.child2 = QuaternaryTreeNode(value)
            return self.child2
        elif self.child3 is None:
            self.child3 = QuaternaryTreeNode(value)
            return self.child3
        elif self.child4 is None:
            self.child4 = QuaternaryTreeNode(value)
            return self.child4
        else:
            raise Exception("이 노드의 모든 자식이 이미 채워져 있습니다.")


"""

def simulates(boardList, level, visited):   
    parms = []
    for List in boardList:
        if List[0][0] == '1':  # 빨간 공이 구멍에 빠지면 종료
            return level
        # 새로운 보드가 이미 방문된 상태라면 그만 처리
        board_tuple = tuple(tuple(row) for row in List)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)  # 방문한 보드 추가
        parms = parms + simulate(List)
    
    if level >= 10 or len(parms) == 0:  # 종료 조건
        return -1
    return simulates(parms, level + 1, visited)

def simulate(board):
    # 상하좌우로 기울인 결과 
    directions = ['up', 'down', 'left', 'right']
    List = []
    for direction in directions:
        new_board = move(board, direction)
        if new_board is not None:
            List.append(new_board)
    
    return List

# 입력 처리
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

visited = set()
print(simulates(simulate(board), 1, visited))
