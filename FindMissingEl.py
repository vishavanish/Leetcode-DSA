# Find the missing value from the list
class missing:
    def findMissing(self,nums):
        
        seen  = set(nums)
        val = []
        for i in range(min(nums), max(nums)):
            if i not in seen:
                val.append(i)

        return val

nums = [1,3,6]
obj = missing()
print(obj.findMissing(nums))



