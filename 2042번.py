def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2 * node, start, mid)
        build_segment_tree(arr, tree, 2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

def update_segment_tree(arr, tree, node, start, end, idx, val):
    if start == end:
        arr[idx] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_segment_tree(arr, tree, 2 * node, start, mid, idx, val)
        else:
            update_segment_tree(arr, tree, 2 * node + 1, mid + 1, end, idx, val)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

def query_segment_tree(tree, node, start, end, L, R):
    if R < start or end < L:
        return 0
    if L <= start and end <= R:
        return tree[node]
    mid = (start + end) // 2
    left_sum = query_segment_tree(tree, 2 * node, start, mid, L, R)
    right_sum = query_segment_tree(tree, 2 * node + 1, mid + 1, end, L, R)
    return left_sum + right_sum

N, K, M = map(int, input().split())
List = [int(input()) for _ in range(N)]

tree = [0] * (4 * N)
build_segment_tree(List, tree, 1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update_segment_tree(List, tree, 1, 0, N - 1, b - 1, c)
    else:
        print(query_segment_tree(tree, 1, 0, N - 1, b - 1, c - 1))