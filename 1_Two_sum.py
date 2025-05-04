class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=[]#Initialize an empty list to store the indices of the two numbers that add up to the target
        for i in range(len(nums)): #Loop through each element in the list using index i 
            for j in range(i+1,len(nums)): # Loop through the elements after index i using index j

                if nums[i]+nums[j]==target: # Check if the sum of the two elements equals the target
                    output.append(i) # If yes, append the index i to the output list
                    output.append(j) # Then append the index j to the output list
                    
        return output     # Return the list containing the two indices

        