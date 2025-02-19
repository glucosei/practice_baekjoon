from collections import Counter

def most_frequent_number(lst):
    if not lst:
        return None, []  # 리스트가 비어있으면 None과 빈 리스트 반환
    counter = Counter(lst)
    most_common = counter.most_common(1)  # 가장 많이 등장하는 요소를 찾음
    most_common_list = [[item, count] for item, count in counter.items()]
    return most_common[0][0], most_common_list  # 요소의 값과 2차원 리스트 반환

def sort_by_difference(two_d_list):
    return sorted(two_d_list, key=lambda x: abs(x[0] - x[1]))

def merge_common_lists(lists):
    merged_counter = Counter()
    for lst in lists:
        for item, count in lst:
            merged_counter[item] += count
    return [[item, count] for item, count in merged_counter.items()]

def compareMemo(memo, lst):
    for mem in memo:
        if mem['sublist'] == lst:
            return mem['result']
    return None

def split_intervals(intervals):
    included_intervals = []
    not_included_intervals = []

    for i, interval in enumerate(intervals):
        is_included = False
        for j, other_interval in enumerate(intervals):
            if i != j and other_interval[0] <= interval[0] and other_interval[1] >= interval[1]:
                is_included = True
                break
        if is_included:
            included_intervals.append(interval)
        else:
            not_included_intervals.append(interval)

    return included_intervals, not_included_intervals

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
QList = []
for _ in range(Q):
    QList.append(list(map(int, input().split())))

sortedQList = sort_by_difference(QList)

results = [None] * Q
memo = []

for List in sortedQList:
    sublist = A[List[0]-1:List[1]]
    memo_result = compareMemo(memo, sublist)
    if memo_result is not None:
        results[QList.index(List)] = memo_result
    else:
        most_frequent, most_common_list = most_frequent_number(sublist)
        results[QList.index(List)] = most_frequent
        memo.append({'sublist': sublist, 'result': most_frequent, 'common_list': most_common_list})

# 구간 병합
merged_intervals = merge_common_lists([memo_item['common_list'] for memo_item in memo])

for result in results:
    print(result)