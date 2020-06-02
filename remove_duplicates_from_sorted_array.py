class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        start = 100000
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                if i<start:
                    start = i
                i = i+1
            if i!=len(nums)-1 and nums[i]!=nums[i+1]:                
                del nums[start:i]
                if start == 100000:
                    i = i+ 1
                if start != 100000:
                    i = start+1
                start = 100000
            if i==len(nums)-1:
                if nums[i]==nums[i-1]:
                    del nums[start:i]
        return(len(nums))               
