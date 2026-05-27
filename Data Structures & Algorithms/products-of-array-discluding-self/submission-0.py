class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        running = 1
        for idx in range(len(nums)):
            output[idx] *= running
            running *= nums[idx]

        running = 1
        for idx in range(len(nums)-1,-1,-1):
            output[idx] *= running
            running *= nums[idx]

        return output

        

        