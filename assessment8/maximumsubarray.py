def binary_search(nums: list[int], target: int) -> tuple[int, int]:

    low = 0
    high = len(nums) - 1
    comparisons = 0
    real_index = -1

    while low <= high:
        guess = (low + high) // 2
        comparisons += 1

        if nums[guess] == target:
            real_index = guess
            high = guess - 1
        elif nums[guess] < target:
            low = guess + 1
        else:
            high = guess - 1

    return real_index, comparisons

print(binary_search([1, 3, 3, 3, 5, 8], 3))


