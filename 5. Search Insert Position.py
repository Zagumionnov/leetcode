
lst = [1, 2, 4, 5, 9, 10, 12, 18, 22]


def search_insert(nums: list[int], target: int) -> int:

    left = 0
    right = len(nums) - 1
    middle_idx = len(nums) // 2

    while nums[middle_idx] != target and left <= right:
        if nums[middle_idx] < target:
            left = middle_idx + 1
        else:
            right = middle_idx - 1

        middle_idx = (left + right) // 2

    return middle_idx if not left > right else middle_idx + 1


print(search_insert(lst, 23))
