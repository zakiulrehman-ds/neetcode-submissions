class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preDic = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in preDic:
                return [preDic[diff], i]
            preDic[n] = i
        return