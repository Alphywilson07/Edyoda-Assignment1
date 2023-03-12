def sort_tuple_list(tuple_list):
    # Sort the list by the last element of each tuple using a for loop
    for i in range(len(tuple_list)):
        for j in range(i+1, len(tuple_list)):
            if tuple_list[i][-1] > tuple_list[j][-1]:
                tuple_list[i], tuple_list[j] = tuple_list[j], tuple_list[i]
    return tuple_list


tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sort_tuple_list(tuple_list)
print(sorted_list)