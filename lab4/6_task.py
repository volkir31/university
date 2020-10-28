count_country = int(input())
country_dict = {}
for _ in range(count_country):
    input_str = input().split()
    country_dict[input_str[0]] = input_str[1:]
count_cities = int(input())
cities_list = []
for _ in range(count_cities):
    cities_list.append(input())
output_list = []
for city in cities_list:
    for country, city1 in country_dict.items():
        if city in city1:
            output_list.append(country)
for item in output_list:
    print(item)
