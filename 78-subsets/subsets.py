class Solution(object):
    def subsets(self, nums):
        ans = []
        subsets = 1<<len(nums)
        for num in range(subsets):
                sub = []
                for j in range(len(nums)):
                    if(num & (1<<j)) :
                        sub.append(nums[j])
                ans.append(sub)
        return ans
    



                

        