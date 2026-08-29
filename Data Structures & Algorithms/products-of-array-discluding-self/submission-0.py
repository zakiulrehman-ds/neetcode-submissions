class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the output array filled with 1s
        res = [1] * len(nums)
        
        # Step 1: Calculate prefix products (going left to right)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate postfix products and combine (going right to left)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
        