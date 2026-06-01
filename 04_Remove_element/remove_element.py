def remove_element(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


n = int(input("How many numbers do you want to enter? "))
nums = []

for i in range(n):
    item = int(input(f"Enter number {i+1}: "))
    nums.append(item)

print(nums)

val = int(input("Which number do you want to remove? "))

print(remove_element(nums, val))