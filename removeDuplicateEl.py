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

nums = [1,3,6,3,7,7,1,2,8]
obj = unique()
print(obj.removeDuplicate(nums))



