def search_insert_postion(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] >= target:
            left = mid
            right = mid-1
        else:
            left = mid + 1
    
    return left


n = int(input("How many numbers do you want to enter? "))
nums = []

for i in range(n):
    item = int(input(f"Enter number {i+1}: "))
    nums.append(item)

print(nums)

target = int(input("Enter target element? "))

print(search_insert_postion(nums, target))