class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        s="aacecaaa"
        if s == s[::-1]:
            return s  # Already a palindrome

    # Instead of slicing and checking each time, reverse once
        rev = s[::-1] #aaacecaa

    # Try to match the longest prefix of s with a suffix of rev
        for i in range(len(s)):
            if s.startswith(rev[i:]):
            # Add the non-matching part of rev to the front
                return rev[:i] + s

        return "" 