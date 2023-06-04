from random import random

def build_items(n):
    res= []
    for i in range(n):
        res.append((i, 1+int(9*random()), 1+int(9*random())))
    return res

def powerset(items):
	res = [[]]
	for item in items:
		newset = [r+[item] for r in res]
		res.extend(newset)
	return res

def weight(item):
	return item[1]

def value(item):
	return item[2]

def knapsack_brute_force01(items, max_weight):
	knapsack = []
	best_weight = 0
	best_value = 0
	for item_set in powerset(items):
		set_weight = sum(map(weight, item_set))
		set_value = sum(map(value, item_set))
		if set_value > best_value and set_weight <= max_weight:
			best_weight = set_weight
			best_value = set_value
			knapsack = item_set
	return knapsack, best_weight, best_value

def knapsack_brute_force_fractional(items, max_weight):
    items.sort(key=lambda item: value(item) / weight(item), reverse=True)

    knapsack = []
    current_weight = 0
    current_value = 0

    for item in items:
        if current_weight + weight(item) <= max_weight:
            knapsack.append(item)
            current_weight += weight(item)
            current_value += value(item)
        else:
            remaining_weight = max_weight - current_weight
            fraction = remaining_weight / weight(item)
            knapsack.append((item[0], remaining_weight, value(item) * fraction))
            current_weight += remaining_weight
            current_value += value(item) * fraction
            break

    return knapsack, current_weight, current_value

items = build_items(3)
max_weight = 10

print("------------0/1 Knapsack Bruteforce------------")
result_01 = knapsack_brute_force01(items, max_weight)
print(result_01)
print("Knapsack items:", result_01[0])
print("Total weight:", result_01[1])
print("Total value:", result_01[2])

print("------------Fractional Knapsack Bruteforce------------")
result_fractional = knapsack_brute_force_fractional(items, max_weight)
print(result_fractional)
print("Fractional Knapsack - Knapsack items:", result_fractional[0])
print("Fractional Knapsack - Total weight:", result_fractional[1])
print("Fractional Knapsack - Total value:", result_fractional[2])


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
print("\n------------Fractional Knapsack Greedy------------")
print(result)
print("Knapsack items:", result[0])
print("Total weight:", result[1])
print("Total value:", result[2])




def weight(item):
    return item[1]

def value(item):
    return item[2]

def bound(node, items, max_weight, n):
    if node[0] >= max_weight:
        return 0

    value_bound = node[1]
    total_weight = node[0]
    j = node[2] + 1

    while j < n and total_weight + weight(items[j]) <= max_weight:
        total_weight += weight(items[j])
        value_bound += value(items[j])
        j += 1

    if j < n:
        value_bound += (max_weight - total_weight) * (value(items[j]) / weight(items[j]))

    return value_bound

def knapsack_branch_and_bound(items, max_weight):
    n = len(items)
    items.sort(key=lambda item: value(item) / weight(item), reverse=True)

    queue = []
    best_node = ([0, 0, -1], 0)  # (current_node, current_value)

    root_node = ([0, 0, -1], 0)
    queue.append(root_node)

    while queue:
        current_node, current_value = queue.pop(0)

        if current_value > best_node[1]:
            best_node = (current_node, current_value)

        level = current_node[2] + 1

        if level < n:
            item = items[level]

            # Include the next item
            new_weight = current_node[0] + weight(item)
            new_value = current_node[1] + value(item)
            new_node = [new_weight, new_value, level]
            queue.append((new_node, new_value))

            # Exclude the next item
            bound_value = bound(current_node, items, max_weight, n)
            if bound_value > best_node[1]:
                queue.append(([current_node[0], current_node[1], level], current_value))

    knapsack = []
    total_weight = best_node[0][0]
    total_value = best_node[1]
    for i in range(n):
        if i <= best_node[0][2]:
            knapsack.append(items[i])

    return knapsack, total_weight, total_value

items = [(0, 2, 5), (1, 4, 10), (2, 3, 7)]
max_weight = 10

result = knapsack_branch_and_bound(items, max_weight)
print("\n------------Knapsack Branch and Bound------------")
print(result)
print("Knapsack items:", result[0])
print("Total weight:", result[1])
print("Total value:", result[2])
