class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        def search(first=1, res = []):
            if len(res) == k:
                output.append(res[:])
            for i in range(first, n+1):
                res.append(i)
                search(i+1)
                res.pop()
        search()
        return output