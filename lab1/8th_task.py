money_dict = {
    '20': 0,
    '10': 0,
    '5': 0,
    '1': 0
}
amount = int(input())
if amount // 20 > 0:
    money_dict['20'], amount = money_dict['20'] + amount // 20, amount % 20
if amount // 10 > 0:
    money_dict['10'], amount = money_dict['10'] + amount // 10, amount % 10
if amount // 5 > 0:
    money_dict['5'], amount = money_dict['5'] + amount // 5, amount % 5
if amount // 1 > 0:
    money_dict['1'], amount = money_dict['1'] + amount // 1, amount % 1
print(money_dict)
