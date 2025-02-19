
def twoPointer(N, List):
    left , right = 0,  len(List) - 1
    bestSum = float('inf')
    best = (List[left], List[right])
    
    while left<right:
        sum = List[left] + List[right]
        if abs(sum) < abs(bestSum):
            bestSum = sum
            best = (List[left], List[right])
        if sum < 0:
            left += 1
        else:
            right -= 1

    return best

N  =int(input())
List = list(map(int, input().split()))
print(*twoPointer(N, List))
