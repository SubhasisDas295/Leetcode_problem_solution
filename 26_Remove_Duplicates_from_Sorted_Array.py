class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums=[0,0,1,1,1,2,2,3,3,4]
        k=0
        for i in range(1,len(nums)):  #1
            if nums[i]!=nums[k]:      # 1!=0
                k+=1           #k=1
                nums[k]=nums[i]  #[0,1,1,1,1,2,2,3,3,4]
        return k+1