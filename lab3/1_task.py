import re

input_string = input()
results_of_search = re.findall(r"\w*\S", input_string)
print(len(results_of_search))
