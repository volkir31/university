input_list = input().split()
count_of_pins, number_of_throws = input_list[0], input_list[1]
list_of_pins = ['|' for i in range(int(count_of_pins))]
knocked_down_pins = 0
for i in range(int(number_of_throws)):
    knocked_down_pins = input().split()
    for j in range(int(knocked_down_pins[0]) - 1, int(knocked_down_pins[1])):
        list_of_pins[j] = '.'

print(''.join(list_of_pins))