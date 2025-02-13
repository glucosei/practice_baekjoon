def digit_sum(n):
    if n == 0:
        return 0
    
    result = 0
    length = len(str(n))
    
    for i in range(length):
        power = 10 ** i
        higher = n // (power * 10)
        current = (n // power) % 10
        lower = n % power
        
        # 1. 현재 자리보다 작은 숫자들 (0~current-1)
        result += higher * 45 * power
        result += (current * (current - 1) // 2) * power  
        
        # 2. 현재 자리에서 남은 lower 부분
        result += current * (lower + 1)
    
    return result

# 입력 받기
L, U = input().split()
L, U = int(L), int(U)

# L-1을 처리하여 정확한 범위 계산
print(digit_sum(U) - digit_sum(L - 1))
