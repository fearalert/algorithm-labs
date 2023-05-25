def weight(item):
	return item[1]

def value(item):
	return item[2]

def knapsack_dynamic(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight_i = weight(items[i - 1])
        value_i = value(items[i - 1])

        for w in range(1, max_weight + 1):
            if weight_i <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight_i] + value_i)
            else:
                dp[i][w] = dp[i - 1][w]

    knapsack = []
    total_weight = 0
    total_value = dp[n][max_weight]
    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = items[i - 1]
            knapsack.append(item)
            total_weight += weight(item)
            w -= weight(item)
    return knapsack, total_weight, total_value
 
items = [(0, 5, 10), (1, 10, 30), (2, 3, 15)]
max_weight = 10

result = knapsack_dynamic(items, max_weight)
print("\n------------Knapsack Dynamic------------")
print(result)
print("Knapsack items:", result[0])
print("Total weight:", result[1])
print("Total value:", result[2])