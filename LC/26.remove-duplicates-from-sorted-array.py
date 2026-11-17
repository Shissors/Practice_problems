#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        s=0
        for f in range(1, len(nums)):
            if nums[f]!=nums[s]:
                s+=1
                nums[s]=nums[f]
        return s+1
    
# @lc code=end

