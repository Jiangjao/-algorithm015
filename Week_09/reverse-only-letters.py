class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 运用栈
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)  