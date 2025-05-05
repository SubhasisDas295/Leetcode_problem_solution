class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1

        rev = int(str(abs(x))[::-1]) * sign          # Reverse the digits of the absolute value of x using string slicing

        return rev if -2**31 < rev < 2**31-1 else 0  # Return the reversed number only if it's within 32-bit signed integer range
