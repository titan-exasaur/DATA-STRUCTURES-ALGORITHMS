class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = nums[(i + nums[i]) % n]
        return res