import itertools

def tsp(cities, start_city):
    num_cities = len(cities)
    all_cities = set(range(num_cities))
    min_distance = float('inf')
    optimal_route = []

    # Generate all possible permutations of cities to visit
    for perm in itertools.permutations(all_cities - {start_city}):
        route = [start_city] + list(perm) + [start_city]
        total_distance = 0

        # Calculate the total distance for the current route
        for i in range(num_cities):
            current_city = route[i]
            next_city = route[i + 1]
            total_distance += cities[current_city][next_city]

        # Update the minimum distance and optimal route if necessary
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_route = route

    return min_distance, optimal_route


cities = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
start_city = 0

min_distance, optimal_route = tsp(cities, start_city)

print("Optimal Route:", optimal_route)
print("Min Distance:", min_distance)
