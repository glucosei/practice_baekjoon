#2261: 가장 가까운 두 점

import sys
import math

def closest_pair(points):
    def distance(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def brute_force(points):
        min_dist = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                min_dist = min(min_dist, distance(points[i], points[j]))
        return min_dist

    def closest_split_pair(px, py, delta):
        mid_x = px[len(px) // 2][0]
        in_strip = [p for p in py if mid_x - delta <= p[0] <= mid_x + delta]
        min_dist = delta

        for i in range(len(in_strip)):
            for j in range(i + 1, min(i + 7, len(in_strip))):
                if (in_strip[j][1] - in_strip[i][1])**2 >= min_dist:
                    break
                min_dist = min(min_dist, distance(in_strip[i], in_strip[j]))
        return min_dist

    def divide_and_conquer(px, py):
        if len(px) <= 3:
            return brute_force(px)

        mid = len(px) // 2
        qx = px[:mid]
        rx = px[mid:]
        mid_x = px[mid][0]

        qy = [p for p in py if p[0] <= mid_x]
        ry = [p for p in py if p[0] > mid_x]

        delta_left = divide_and_conquer(qx, qy)
        delta_right = divide_and_conquer(rx, ry)
        delta = min(delta_left, delta_right)

        return min(delta, closest_split_pair(px, py, delta))

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])

    return divide_and_conquer(px, py)

# 빠른 입력
input = sys.stdin.read
data = input().split()
N = int(data[0])
points = []
for i in range(N):
    x, y = int(data[2 * i + 1]), int(data[2 * i + 2])
    points.append((x, y))

# 결과 출력
result = closest_pair(points)
print(result)
