count_of_cards = int(input())
sum_number_on_cards = 0
for number_on_card in range(1, count_of_cards+1):
    sum_number_on_cards += number_on_card
sum_without_one_card = 0
for iter in range(count_of_cards-1):
    card = int(input())
    sum_without_one_card += card
print(sum_number_on_cards - sum_without_one_card)
