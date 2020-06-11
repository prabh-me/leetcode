class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        words = s.split(" ")
        max = 0
        for i in words:
            if len(i)!=0:
                max = len(i)
        return max
