#kmp알고리즘(주기성에 기반을 둔 k = k-T)


"""
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors, reverse=True)


def get_str_power(S):
    n = len(S)
    divisors = get_divisors(n)
    for i in divisors:
        correct = True
        for j in range(0, n-(n//i), n//i):
            if S[j:j + n//i] != S[j+(n//i):j+2*(n//i)]:
                correct = False
                break
        if correct == True:
            return i
    return 1
            
        


SList = []
run = 1
while run == 1:
    S = input()
    if S == ".":
        run = 0
    else:
        SList.append(S)
        

for i in SList:
    print(get_str_power(i))
"""

def compute_failure_function(S):
    n = len(S)
    failure = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and S[i] != S[j]:
            j = failure[j - 1]
        if S[i] == S[j]:
            j += 1
            failure[i] = j

    return failure

def get_str_power(S):
    n = len(S)
    failure = compute_failure_function(S)
    length_of_pattern = n - failure[-1]

    if n % length_of_pattern == 0:
        return n // length_of_pattern
    else:
        return 1

SList = []
run = True
while run:
    S = input()
    if S == ".":
        run = False
    else:
        SList.append(S)

for i in SList:
    print(get_str_power(i))