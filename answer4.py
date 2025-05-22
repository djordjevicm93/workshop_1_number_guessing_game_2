def div(begin_r, end_r):
    result_l = list()
    for n in range(int(begin_r), int(end_r) + 1):
        if n % 2 == 0 and n % 3 != 0:
            result_l.append(n)
    return result_l

result = div(0, 20)
print(result)  # [2, 4, 8, 10, 14, 16, 20]
