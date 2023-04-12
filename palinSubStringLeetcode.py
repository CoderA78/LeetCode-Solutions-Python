class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s       
        # initialize start and end indices of the longest palindrome
        start, end = 0, 0
        # check all possible centers of palindromes
        for i in range(n):
            # check odd-length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1
            # check even-length palindromes
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > end - start:
                    start, end = l, r
                l -= 1
                r += 1
        # return the longest palindromic substring
        return s[start:end+1]
    
sol= Solution()
print(sol.longestPalindrome("abracecarsracecar"))