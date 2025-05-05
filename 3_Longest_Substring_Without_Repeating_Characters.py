class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s="abcabcbb"
        if len(set(s))==len(s):   #len(set(s))=3 and len(s)=6    so it false
            return len(s)
        
        substring=''    # bb
        max_length=1    # 3

        for i in s:                    # b
            if i not in substring:     # c not in substring
                substring=substring+i  # cb
                max_length=max(max_length,len(substring))  # 3
            else:                                          # b already there in substring
                substring=substring.split(i)[1]+i          # substring= ["b","b"] and
                                                           # new substring = "b" + "" = "b"
        return max_length                                         