class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if len(s) == 0:
            return 0

        i = 0
        sign = 1
        num = 0

        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():

            digit = ord(s[i]) - ord('0')

            if num > 214748364 or (num == 214748364 and digit > 7):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648

            num = num * 10 + digit

            i += 1

        return num * sign