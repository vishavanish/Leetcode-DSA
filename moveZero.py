def moveZero(nums):
    
    right = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[right], nums[i] = nums[i], nums[right]
            right += 1

    
    print(nums)

nums = [0, 1, 0, 3, 0]
moveZero(nums)

#==============================================================
def moveZero(nums):
    left  =0
    right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    print(nums)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
moveZero(nums)
