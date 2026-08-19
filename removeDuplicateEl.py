# remove duplicate from the list
class unique:
    def removeDuplicate(self,nums):
        
        seen  = []
        j = 0
        for i in nums:
            if i not in seen:
                seen.append(i)
                nums[j] = i
                j += 1
        del nums[j:]
        return nums

nums = list(map(int, input("Enter numbers separated by space: ").split()))
obj = unique()
print(obj.removeDuplicate(nums))



