class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if a + nums[j] == target:
                    return [i, j]
        return []