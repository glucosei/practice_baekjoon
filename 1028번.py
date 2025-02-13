def largest_diamond(mine):
    R = len(mine)
    C = len(mine[0])
    
    # dp 배열 초기화
    dp_left = [[0] * C for _ in range(R)]
    dp_right = [[0] * C for _ in range(R)]
    dp_up = [[0] * C for _ in range(R)]
    
    # 각 위치에서 가능한 최대 다이아몬드 크기 계산
    for i in range(R):
        for j in range(C):
            if mine[i][j] == 1:
                if i == 0 or j == 0:
                    dp_left[i][j] = 1
                else:
                    dp_left[i][j] = dp_left[i-1][j-1] + 1
                
                if i == 0 or j == C - 1:
                    dp_right[i][j] = 1
                else:
                    dp_right[i][j] = dp_right[i-1][j+1] + 1
                
                if i == 0:
                    dp_up[i][j] = 1
                else:
                    dp_up[i][j] = dp_up[i-1][j] + 1
    
    max_diamond = 0
    for i in range(R):
        for j in range(C):
            size = min(dp_left[i][j], dp_right[i][j], dp_up[i][j])
            while size > max_diamond:
                if i - 2 * (size - 1) >= 0 and dp_left[i - (size - 1)][j] >= size and dp_right[i - (size - 1)][j] >= size:
                    max_diamond = size
                size -= 1
    
    return max_diamond

# 입력 받기
R, C = map(int, input().split())
mine = []
for _ in range(R):
    mine.append(list(map(int, input().strip())))

# 가장 큰 다이아몬드 크기 출력
print(largest_diamond(mine))