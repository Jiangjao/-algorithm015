class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        count = s.split()
        for word in reversed(count):
            res = res +' '+word

        return res.lstrip()