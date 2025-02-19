
def findPrime(N):
    is_prime = [True] * (N + 1)
    p = 2
    while (p * p <= N):
        if (is_prime[p] == True):
            for i in range(p * p, N + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, N + 1) if is_prime[p]]
    return prime_numbers

N = int(input())
prime_numbers = findPrime(N)

start = 0
end = 0
sum = 0
count = 0

while True:
    if sum >= N:
        sum -= prime_numbers[start]
        start += 1
    elif end == len(prime_numbers):
        break
    else:
        sum += prime_numbers[end]
        end += 1
    if sum == N:
        count += 1
    

print(count)