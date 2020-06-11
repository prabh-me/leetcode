class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        currentsum = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            currentsum = max(currentsum+nums[i], nums[i])
            if currentsum > maxsum:
                maxsum = currentsum
        return maxsum
