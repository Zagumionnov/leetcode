

def remove_element(nums: list[int], val: int) -> int:
    while True:
        if val in nums:
            nums.remove(val)
        else:
            break
    return len(nums)


value = 3
numbers = [3, 3]
print(len(numbers))
print(remove_element(numbers, value))
