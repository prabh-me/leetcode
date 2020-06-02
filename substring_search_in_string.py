class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        match = 1
        count = 0
        if len(needle)==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                index = i
                count = 0
                for j in range(len(needle)):
                    if i+j>=len(haystack):
                        match=0
                        break
                    if needle[j] != haystack[i+j]:
                        match = 0
                        break
                    if needle[j] == haystack[i+j]:
                        count = count + 1
                if count == len(needle):
                    match = 1
                if match == 1:
                    break
        if count == len(needle):
            return index
        if count != len(needle):
            return -1
    
                
                
           
            
