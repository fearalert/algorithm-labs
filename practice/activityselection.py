def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m += 1

    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


# Define activities with start time and end time
start_time = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
end_time = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
n = len(start_time) - 1
k = 0

# Call the recursive_activity_selector function
selected_activities = recursive_activity_selector(start_time, end_time, k, n)

# Print the selected activities
print("Selected Activities:")
for activity_index in selected_activities:
    print(f"Start time: {start_time[activity_index]}, End time: {end_time[activity_index]}")
