def even(list_numbers):
    return list_numbers%2 == 1
numbers = range(1,11)
filtered_numbers=list(filter(even,numbers))

print(filtered_numbers)
