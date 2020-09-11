mark_dict = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0
}
digit_mark = 0
count_mark = 0
while True:
    mark = input().upper()
    if mark == 'Q':
        break
    else:
        digit_mark += mark_dict[mark]
        count_mark += 1
print(
    round(digit_mark / count_mark, 2) if str(round(digit_mark / count_mark, 2))[-1] != '0' else round(digit_mark /
                                                                                                      count_mark, 1))
