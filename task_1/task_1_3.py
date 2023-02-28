class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        check_greatest = []
        for i in candies:
            if (i + extraCandies) >= max(candies):
                check_greatest.append(True)
            else:
                check_greatest.append(False)
        return check_greatest