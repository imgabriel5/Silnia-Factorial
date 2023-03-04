# Przygotuj funkcję, która będzie zamieni wszystkie elementy listy na stringi oraz drugą, która
# zamieni każdy element listy na integer.
# Prepare a function that will convert all elements of the list to strings, and another that will
# will convert each element of the list to an integer.
print('-----------------------------------------------------------------------------------------------------')
# 1.
def change_to_string(items):
    return [str(item) for item in items]

def change_to_integer(items):
    return [int(item) for item in items if item.isdigit()]

print(change_to_string(['1', '2', '3']))
print(change_to_integer(['1', '2', '3']))
print('-----------------------------------------------------------------------------------------------------')
# 2.
def convert_strs_to_ints(list_of_strings: list) -> list:
    return list(map(int, list_of_strings))

def convert_ints_to_strs(list_of_ints: list) -> list:
    return list(map(str, list_of_ints))

print(convert_ints_to_strs(['1', '2', '3']))
print(convert_strs_to_ints(['1', '2', '3']))