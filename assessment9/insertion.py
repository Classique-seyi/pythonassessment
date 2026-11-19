def insertion_sort(nums: list):
    comparisons = 0
    shifts = 0
    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            comparisons += 1
            nums[j + 1] = nums[j]
            print(f"comparisons:{comparisons} {nums}")
            j -= 1

        nums[j + 1] = current
        shifts += 1
        print(f"shifts: {nums}")

    return nums

print(insertion_sort([5, 2, 4, 1]))
        

