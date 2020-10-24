class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            # ret = ret | (((n >> (31-i))  & 1)<< i)
            ret = ret | (((n >> (31-i)) & 1 ) << i)
        return ret