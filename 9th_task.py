distance_per_day, required_distance = int(input()), int(input())
if distance_per_day > required_distance:
    print(1)
elif required_distance % distance_per_day == 0:
    print(required_distance // distance_per_day)
else:
    print(1 + required_distance // distance_per_day)
