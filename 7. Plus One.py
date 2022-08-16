
ex_one = [1, 2, 3]
ex_two = [9]
ex_tree = [1, 9, 9, 9]


def plus_one(digits: list[int]) -> list[int]:
    for idx, val in enumerate(digits[::-1]):
        if val == 9:
            digits[-(idx+1)] = 0
            if idx+1 == len(digits):
                return [1] + digits
            continue
        else:
            digits[-(idx+1)] += 1
            return digits



print(plus_one(ex_one))

# def plus_one(digits: list[int]) -> list[int]:
#     num = 0
#     for i in range(len(digits)):
#         num += digits[i] * pow(10, (len(digits) - 1 - i))
#     return [int(i) for i in str(num + 1)]
