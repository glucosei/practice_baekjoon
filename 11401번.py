MOD = 1000000007

def mod_inverse(a, p):
    return pow(a, p - 2, p)

def binomial_coefficient(N, K, MOD):
    if K > N:
        return 0
    if K == 0 or K == N:
        return 1

    # 팩토리얼 계산
    fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD

    # 이항계수 계산
    numerator = fact[N]
    denominator = (fact[K] * fact[N - K]) % MOD
    return numerator * mod_inverse(denominator, MOD) % MOD

# 입력 받기
N, K = map(int, input().split())
print(binomial_coefficient(N, K, MOD))