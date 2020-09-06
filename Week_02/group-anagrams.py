class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 映射/
        dic =  {}
        for s in strs:
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s]
        return dic.values()
        