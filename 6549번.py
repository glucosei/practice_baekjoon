def largest_rectangle_area(histogram):
    stack = []
    max_area = 0
    index = 0

    while index < len(histogram):
        if not stack or histogram[stack[-1]] <= histogram[index]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while index < len(data):
        n = int(data[index])
        if n == 0:
            break
        histogram = list(map(int, data[index + 1:index + 1 + n]))
        print(largest_rectangle_area(histogram))
        index += n + 1

if __name__ == "__main__":
    main()