class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        for i in range(len(s)):
            # odd length palindrome
            offset = 0
            while i-offset >= 0 and i+offset < len(s) and s[i-offset] == s[i+offset]:
                if (2*offset + 1) > max_len:
                    res = s[i-offset:i+offset+1]
                    max_len = max(max_len, 2*offset + 1)
                offset += 1

            # even length palindrome
            offset = 0
            while i-offset >= 0 and i+1+offset < len(s) and s[i-offset] == s[i+1+offset]:
                if (2*offset + 2) > max_len:
                    res = s[i-offset:i+offset+2]
                    max_len = max(max_len, 2*offset + 2)
                offset += 1
        
        return res

