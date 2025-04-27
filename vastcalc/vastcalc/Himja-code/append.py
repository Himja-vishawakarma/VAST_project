def append(lst, item):
    new_list = [None] * (len(lst) + 1)
    
    for i in range(len(lst)):
        new_list[i] = lst[i]

    new_list[len(lst)] = item
    return new_list

my_list = [10, 20, 30]
m= my_list.append(50)
print(m)
print(my_list)