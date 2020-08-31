class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = {}
        length = len(s)
        if length != len(t): return False
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in t:
            if j in count:
                count[j] -= 1
                length -= 1
                if count[j] < 0:
                    return False
            else:
                return False
        return length == 0