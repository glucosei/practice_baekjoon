
L1 = input().strip()
L2 = input().strip()

len1, len2 = len(L1), len(L2)

# DP 테이블 초기화
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# DP 테이블 채우기
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if L1[i - 1] == L2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 최장 공통 부분 수열의 길이
longest = dp[len1][len2]
print(longest)

# 최장 공통 부분 수열 찾기
lcs = []
i, j = len1, len2
while i > 0 and j > 0:
    if L1[i - 1] == L2[j - 1]:
        lcs.append(L1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

# LCS는 역순으로 저장되었으므로 뒤집어서 출력
print(''.join(reversed(lcs)))