class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""     # Store the longest palindrome substring
        max_length=0  # Keep track of the maximum length of palindrome found
        if len(s)<2:
            return s
        # Loop through all possible substrings
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring=s[i:j+1]      # Get the substring from i to j
                if substring == substring[::-1]:   # Check if it's a palindrome
                    if len(substring)>max_length:  # If it's longer than previous ones
                        max_length=len(substring)
                        result=substring           # Update result with the new longest palindrome
        return result
    