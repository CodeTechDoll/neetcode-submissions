class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix: List[int] = [1] * n
        suffix: List[int] = [1] * n

        product = 1
        for i in range(n):
            prefix[i] = product
            product *= nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        result = []

        for i in range(n):
            result.append(prefix[i] * suffix[i])

        return result