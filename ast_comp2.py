import ast

x = r'''def knapsack(capacity, items):
    from collections import defaultdict
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            if weight <= j:
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]'''

y = r'''def knapsack(capacity, items):
    memo = [0] * (capacity + 1)  # 1D array for memoization

    for item in items:
        weight, value = item
        for j in range(capacity, weight - 1, -1):
            memo[j] = max(memo[j], memo[j - weight] + value)

    return memo[capacity]'''

xd = ast.dump(ast.parse(x))
yd = ast.dump(ast.parse(y))
print(xd == yd)
