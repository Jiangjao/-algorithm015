class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        for i in s:
            res[i] = res.get(i, 0) + 1
        
        for idx, ch in enumerate(s):
            if res[ch] == 1:
                return idx
        return -1