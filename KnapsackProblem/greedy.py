def weight(item):
	return item[1]

def value(item):
	return item[2]

def knapsack_greedy(items, max_weight):
    items.sort(key=lambda x: value(x)/weight(x), reverse=True)

    knapsack = []
    total_weight = 0
    total_value = 0

    for item in items:
        if total_weight + weight(item) <= max_weight:
            knapsack.append(item)
            total_weight += weight(item)
            total_value += value(item)
        else:
            remaining_capacity = max_weight - total_weight
            fraction = remaining_capacity / weight(item)
            knapsack.append((item[0], item[1] * fraction, item[2] * fraction))
            total_weight += remaining_capacity
            total_value += value(item) * fraction
            break

    return knapsack, total_weight, total_value

items = [(0, 5, 10), (1, 10, 30), (2, 3, 15)]
max_weight = 10

result = knapsack_greedy(items, max_weight)
print("------------Fractional Knapsack Greedy------------")
print(result)
print("Knapsack items:", result[0])
print("Total weight:", result[1])
print("Total value:", result[2])