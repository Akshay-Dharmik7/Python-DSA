def missing_number(nums):
    ans =((len(nums) + 1))
    ans *=len(nums)
    ans //=2

    for i in nums:
        ans -= i

    return ans

nums = [3,0,1] 
result = missing_number(nums)
print('Missing number is:', result)