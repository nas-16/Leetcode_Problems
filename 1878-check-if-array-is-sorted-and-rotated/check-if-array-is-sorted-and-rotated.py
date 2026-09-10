class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)
        
        # Check adjacent elements
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                
        # Check the wrap-around edge between the last and first element
        if nums[n - 1] > nums[0]:
            count += 1
            
        return count <= 1