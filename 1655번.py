import sys
import heapq

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    left, right = [], []  # left는 max-heap, right는 min-heap
    result = []
    
    
    
    for i in range(1, N+1):
        num = int(data[i])

        
        if not left or num <= -left[0]:
            heapq.heappush(left, -num)  
        else:
            heapq.heappush(right, num)

        
        if len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))
        elif len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

        
        result.append(str(-left[0]))

    
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
