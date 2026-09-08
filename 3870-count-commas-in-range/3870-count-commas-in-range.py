class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            if (i >= 1000 and i <= 100000):
                count = count + 1
        return count
        