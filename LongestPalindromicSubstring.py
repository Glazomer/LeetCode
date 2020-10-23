class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalStart = longestPalEnd = l = r = 0

        while r < len(s):
            if l == r:
                # Looking for the 'root' of palindrome,
                # either odd or even number of same characters
                while r + 1 < len(s) and s[l] == s[r+1]:
                    r += 1
                    if l > 0 and s[l - 1] == s[r]:
                        l -= 1

            if 0 <= l and s[l] == s[r]:
                if ((r+1)-l > longestPalEnd-longestPalStart):
                    longestPalStart = l
                    longestPalEnd = r + 1
                r += 1
                l -= 1
            else:
                l = r = (r + l) // 2 + 1  # going to middle +1 step

        return s[longestPalStart:longestPalEnd]
