def add_one(some_list):
    n = len(some_list)
    a = 1
    for i in range(n -1, -1, -1):
        if a == 0:
            break
        new_value = some_list[i] + a
        if new_value == 10:
            some_list[i] = 0
            a = 1
        else:
            some_list[i] = new_value
            a = 0
    if a == 1:
        some_list.insert(0, 1)
    return some_list
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")