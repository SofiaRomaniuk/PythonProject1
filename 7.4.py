def common_elements():
    multiples_of_3 = [x for x in range(0, 100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(0, 100) if x % 5 == 0]

    result_set = set(multiples_of_3) & set(multiples_of_5)
    return result_set

print(common_elements())