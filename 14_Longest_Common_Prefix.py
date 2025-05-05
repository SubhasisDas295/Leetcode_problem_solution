class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                s+=first[i]
            else:
                break
        return s