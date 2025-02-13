import sys

def tsp(dp, dist, visited, pos, n):
    if visited == (1 << n) - 1:
        return dist[pos][0] if dist[pos][0] > 0 else sys.maxsize

    if dp[visited][pos] != -1:
        return dp[visited][pos]

    min_cost = sys.maxsize
    for city in range(n):
        if visited & (1 << city) == 0 and dist[pos][city] > 0:
            new_cost = dist[pos][city] + tsp(dp, dist, visited | (1 << city), city, n)
            min_cost = min(min_cost, new_cost)

    dp[visited][pos] = min_cost
    return min_cost

def solve_tsp(dist):
    n = len(dist)
    dp = [[-1] * n for _ in range(1 << n)]
    return tsp(dp, dist, 1, 0, n)

# 입력 받기
N = int(input())
W = []
for i in range(N):
    W.append(list(map(int, input().split())))

# 외판원 순회 문제 해결
result = solve_tsp(W)
print(result)