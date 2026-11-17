#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        s=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[s]=nums[i]
                s+=1
        return s
# @lc code=end

