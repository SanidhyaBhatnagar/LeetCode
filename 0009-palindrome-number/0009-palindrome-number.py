class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if x == 0:
            return True

        temp = x
        digits = 0

        while temp != 0:
            digits += 1
            temp = temp // 10

        arr = [0] * digits

        r = digits - 1

        while x != 0:
            mod = x % 10
            x = x // 10

            arr[r] = mod
            r = r - 1

        l = 0
        endr = digits - 1

        while l < endr:

            if arr[l] != arr[endr]:
                return False

            l = l + 1
            endr = endr - 1

        return True