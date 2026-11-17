#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
# @lc code=end

