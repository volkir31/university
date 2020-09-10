distance_per_day, required_distance = int(input()), int(input())
print('1' if distance_per_day > required_distance else 1 + required_distance // distance_per_day)