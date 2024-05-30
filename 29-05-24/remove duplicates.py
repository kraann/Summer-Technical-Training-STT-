def remove_duplicates(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]


input_list = [1, 2, 3, 2, 1, 4, 5, 4]
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)

