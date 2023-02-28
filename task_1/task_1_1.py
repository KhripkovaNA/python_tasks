class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = []
        s = 0
        for n in nums:
            s += n
            rs.append(s)
        return rs