class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
	def dfs(left,right,tmp):
			# 递归函数的终止条件
			if left==n and right==n:
				res.append(tmp)
				return
			# 注意左括号的数量要小于参数n，即输入的n为3时
			# 最多只能生成3个左括号
			if left<n:
				dfs(left+1,right,tmp+"(")
			# 右括号的数量也要小于n，左括号的数量要 大于 右括号数量
			# 因为 ((( 是合法的(假设程序还没处理完)
			# 而),)),)))都是不合法的
			if left>right and right<n:
				dfs(left,right+1,tmp+")")
        dfs(0,0,"")
        return res