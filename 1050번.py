import heapq
import sys
from collections import defaultdict, deque

input = sys.stdin.read
INF = 1000000001

def calculate_costs(market, formulas):
    costs = {name: price for name, price in market.items()}
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for result, ingredients in formulas.items():
        for quantity, name in ingredients:
            graph[name].append((result, quantity))
            indegree[result] += 1
    
    queue = deque([name for name in market])
    
    while queue:
        current = queue.popleft()
        
        for neighbor, quantity in graph[current]:
            if neighbor not in costs:
                costs[neighbor] = 0
            costs[neighbor] += quantity * costs[current]
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return costs

def main():
    data = input().split()
    index = 0
    
    market_count = int(data[index])
    index += 1
    formula_count = int(data[index])
    index += 1
    
    market = {}
    for _ in range(market_count):
        name = data[index]
        price = int(data[index + 1])
        market[name] = price
        index += 2
    
    formulas = defaultdict(list)
    for _ in range(formula_count):
        formula = data[index]
        index += 1
        result, ingredients = formula.split('=')
        ingredients = ingredients.split('+')
        
        for ingredient in ingredients:
            quantity = int(ingredient[0])
            name = ingredient[1:]
            formulas[result].append((quantity, name))
    
    costs = calculate_costs(market, formulas)
    
    result = costs.get('LOVE', INF)
    if result >= INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()