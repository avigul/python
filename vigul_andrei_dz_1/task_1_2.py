def sum_list_1(dataset: list) -> int:
    result = []
    for i in dataset:
        if i // 1 in dataset:
            k = i ** 3
            date = str(k)
            date = [int(i) for i in date]
            sum_date = sum(date)
            remain = sum_date % 7
        if remain == 0:
            result.append(i)
    return sum(result)


def sum_list_2(dataset: list) -> int:
    result = [i + 17 for i in dataset]
    return sum_list_1(result)


my_list = [i for i in range(1, 1001)]
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
