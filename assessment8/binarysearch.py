def binary_search(nums, target):
    if not nums:
        return -1, 0
    if nums[0] == target:
        return 0, 1
    low = 0
    high = len(nums) - 1
    num = []

    while low < high:
        if nums[low] != target:
            return f"(-1, comparisons)"
        else:
            num.append(nums[low])
            return f"({num[0]}, comparisons)"
            
    
        

    
        


print(binary_search([1, 3, 3, 3, 5, 8], 3))
print(binary_search([1, 3, 5, 8], 4))
print(binary_search([], 3))
print(binary_search([5], 0))