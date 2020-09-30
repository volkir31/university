list_of_height, current_height, place = input().split(), input(), 1
for i in range(len(list_of_height)):
    if current_height <= list_of_height[i]:
        place += 1
    else:
        break
print(place)
