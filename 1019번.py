def count_digit_occurrences(n):
    count = [0] * 10  # 0부터 9까지의 등장 횟수를 저장
    digit_place = 1  # 자릿수 (1의 자리부터 시작)

    while digit_place <= n:
        # 현재 자릿수에서의 숫자 분리
        lower_numbers = n - (n // digit_place) * digit_place  # 현재 자릿수보다 낮은 자릿수의 나머지
        current_digit = (n // digit_place) % 10  # 현재 자릿수의 숫자
        higher_numbers = n // (digit_place * 10)  # 현재 자릿수보다 높은 자릿수

        # 각 숫자 0-9에 대해 등장 횟수 계산
        for digit in range(10):
            if digit < current_digit:
                count[digit] += (higher_numbers + 1) * digit_place
            elif digit == current_digit:
                count[digit] += higher_numbers * digit_place + lower_numbers + 1
            else:
                count[digit] += higher_numbers * digit_place
        
        # 0의 특별 처리: 가장 높은 자리에서는 0이 나타날 수 없음
        count[0] -= digit_place  # 0은 숫자의 맨 앞에 등장하지 않음
        
        # 자릿수 증가
        digit_place *= 10

    return count

# 예시 실행
n = int(input())
result = count_digit_occurrences(n)
for i in range(10):
    print(result[i],end = " ")
