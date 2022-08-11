

def removeDuplicates(nums: list[int]) -> int:
    count = 1
    for n in range(len(nums) - 1):
        if nums[n] != nums[n + 1]:
            nums[count] = nums[n + 1]
            count += 1

    return count



# def removeDuplicates(nums: list[int]) -> int:
#     x = 1
#     for i in range(len(nums) - 1):
#         if nums[i] != nums[i + 1]:
#             nums[x] = nums[i + 1]
#             x += 1
#     return x


# def removeDuplicates(nums: list[int]) -> int:
#     count = 0
#     for n in range(len(nums)):
#         if n == 0:
#             count += 1
#             continue
#         if nums[n] != nums[n-1]:
#             count += 1
#     return count


# def removeDuplicates(nums: list[int]) -> int:
#     count = 0
#     for n in range(len(nums)):
#         if nums[n] < nums[n+1]:
#             count += 1
#     return count


nums = [-1, -1, -2, -3, -3, -4, -4, 0, 1, 1, 2]
print(len(nums))
print(removeDuplicates(nums))
