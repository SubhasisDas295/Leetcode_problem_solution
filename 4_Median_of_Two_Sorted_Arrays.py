class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=sorted(nums1+nums2) # Merge the two arrays and sort the combined list

        if len(nums1)%2==0: # If the total number of elements is even
            first_element=len(nums1)/2 #Index of the right middle element(ex. for 6 elements,,index is 3)
            second_element=len(nums1)/2-1 #Index of the left middle element(ex. for 6 elements, index is 2)
            output=(nums1[first_element]+nums1[second_element])/2.0 # Average of the two middle values for even-length list (using float division)

        else: # If the total number of elements is odd
            middle_element=len(nums1)/2  # Middle index (e.g. for 5 elements, index is 2)
            output=float(nums1[middle_element]) # Just taking the middle value and converting it to float

        return output #returning the median