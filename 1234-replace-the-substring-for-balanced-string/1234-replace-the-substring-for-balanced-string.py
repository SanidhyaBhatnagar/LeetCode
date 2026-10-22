
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        count = {
            'Q': 0,
            'W': 0,
            'E': 0,
            'R': 0
        }

        for ch in s:
            count[ch] += 1

        if all(count[ch] == target for ch in count):
            return 0

        l = 0
        ans = n

        for r in range(n):
            count[s[r]] -= 1

            while (count['Q'] <= target and
                   count['W'] <= target and
                   count['E'] <= target and
                   count['R'] <= target):

                ans = min(ans, r - l + 1)

                count[s[l]] += 1
                l += 1

        return ans
