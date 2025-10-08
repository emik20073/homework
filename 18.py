def common_elements():
    multiple_of_3 = [i for i in range(0,100) if i % 3 == 0]
    multiple_of_5 = [i for i in range(0,100) if i % 5 == 0]
    return set(multiple_of_3). intersection(multiple_of_5)
print(common_elements())