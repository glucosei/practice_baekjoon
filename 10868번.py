import sys
sys.setrecursionlimit(10**6)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 세그먼트 트리 저장 배열
        self.arr = arr
        self.build(0, 0, self.n - 1)  # 트리 생성

    def build(self, node, start, end):
        if start == end:  # 리프 노드
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)  # 왼쪽 자식
            self.build(2 * node + 2, mid + 1, end)  # 오른쪽 자식
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])  # 최소값 저장

    def query(self, node, start, end, left, right):
        if right < start or left > end:  # 범위를 벗어난 경우
            return float('inf')
        if left <= start and end <= right:  # 완전히 포함되는 경우
            return self.tree[node]

        mid = (start + end) // 2
        left_min = self.query(2 * node + 1, start, mid, left, right)
        right_min = self.query(2 * node + 2, mid + 1, end, left, right)
        return min(left_min, right_min)

    def range_min(self, left, right):
        return self.query(0, 0, self.n - 1, left, right)


# 입력 처리
N, M = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(N)]  # N개의 정수 입력
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]  # M개의 쿼리 입력

# 세그먼트 트리 생성
st = SegmentTree(arr)

# 쿼리 실행 및 출력
output = []
for a, b in queries:
    output.append(st.range_min(a - 1, b - 1))  # 1-based index를 0-based index로 변환

# 결과 출력
sys.stdout.write('\n'.join(map(str, output)) + '\n')
