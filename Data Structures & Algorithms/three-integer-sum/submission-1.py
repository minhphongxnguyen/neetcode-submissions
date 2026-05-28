class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], target: int) -> List[int]:
            l, r = 0, len(nums) - 1
            pairs = []
            while l < r:
                if l > 0 and nums[l] == nums[l-1]:
                    l += 1
                    continue

                twoSum = nums[l] + nums[r]
                if twoSum > target:
                    r -= 1
                elif twoSum < target:
                    l += 1
                else:
                    pairs.append([nums[l], nums[r]])
                    l += 1

            return pairs

        nums.sort()
        triplets = []
        for idx, n in enumerate(nums):
            if idx > 0 and nums[idx-1] == nums[idx]:
                continue 

            diff = 0 - n
            pairs = twoSum(nums[idx+1:], diff)
            if pairs:
                for p in pairs:
                    triplets.append([n, *p])

        return triplets

            









    
        