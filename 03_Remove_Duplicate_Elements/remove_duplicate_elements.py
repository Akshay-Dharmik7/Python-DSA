def remove_duplicate_elements(nums):
    i = 0
    j = i+1

    if len(nums) == 1:
        return 1
    
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1

            nums[i], nums[j] = nums[j], nums[i]
        
        j += 1
    
    return nums

n = int(input("How many string do you want to enter? "))
nums = []

for i in range(n):
    item = int(input(f"Enter number {i+1}: "))
    nums.append(item)

print(nums)

print(remove_duplicate_elements(nums))