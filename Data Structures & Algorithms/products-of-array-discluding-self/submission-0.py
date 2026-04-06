class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n #initialize 

        #every index has left and right component
        output[0] = 1 #leftmost
        for i in range(1,n):
            output[i] = output[i-1] * nums[i-1]

        R = 1 #right most
        for i in reversed(range(n)):
            output[i] = output[i] * R
            R *= nums[i]

        return output
        