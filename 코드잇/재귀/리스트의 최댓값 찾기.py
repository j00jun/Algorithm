def max_list(my_list):
    if len(my_list) <= 1:
        return my_list[0]
    sublist = max_list(my_list[:-1])
    if sublist >= my_list[-1]:
        return sublist
    else:
        return my_list[-1]

print(max_list([1, 4, 3, 2, 5, 0, 2]))
print(max_list([-1, -3, -10, -5, -9]))
print(max_list([3, 7, 3, 7, 7]))
print(max_list([1, 2.7, -3, 2.8, 1.6]))
print(max_list([32, 2, 3, 0 , 1]))
