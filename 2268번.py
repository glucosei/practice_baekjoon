import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

class SegmentTree:
    def __init__(self, arr):
        """배열을 입력받아 세그먼트 트리를 구축한다."""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 트리 배열 (최대 4N 크기)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """재귀적으로 세그먼트 트리를 구축"""
        if start == end:  # 리프 노드 (배열 값 저장)
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            # 왼쪽, 오른쪽 자식을 재귀적으로 생성
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)

            # 현재 노드 값 = 왼쪽 자식 + 오른쪽 자식
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, start, end, left, right):
        """구간 [left, right]의 합을 반환"""
        if left > end or right < start:
            return 0  # 범위를 벗어난 경우

        if left <= start and end <= right:
            return self.tree[node]  # 현재 구간이 완전히 포함된 경우

        # 부분적으로 겹치는 경우
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, left, right)
        right_sum = self.query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum

    def update(self, node, start, end, idx, value):
        """배열의 특정 값 변경 및 트리 갱신"""
        if start == end:
            self.tree[node] = value  # 리프 노드 갱신
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, value)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, value)

            # 부모 노드 갱신
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def range_sum(self, left, right):
        """구간 합을 구하는 함수 (외부에서 호출)"""
        return self.query(0, 0, self.n - 1, left, right)

    def point_update(self, idx, value):
        """값을 업데이트하는 함수 (외부에서 호출)"""
        self.update(0, 0, self.n - 1, idx, value)

def main():
    input_data = input().split()
    N = int(input_data[0])
    M = int(input_data[1])
    queries = input_data[2:]

    arr = [0] * N
    segTree = SegmentTree(arr)

    result = []
    for i in range(M):
        q_type = int(queries[3 * i])
        a = int(queries[3 * i + 1]) - 1
        b = int(queries[3 * i + 2])
        if q_type == 1:
            segTree.point_update(a, b)
        else:
            result.append(segTree.range_sum(a, b - 1))

    sys.stdout.write('\n'.join(map(str, result)) + '\n')

if __name__ == "__main__":
    main()