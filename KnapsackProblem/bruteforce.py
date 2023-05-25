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