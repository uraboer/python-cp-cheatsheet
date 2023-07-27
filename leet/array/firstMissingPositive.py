class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        return next(
            (i for i in range(1, len(nums)) if i not in s),
            len(nums) if len(nums) not in s else len(nums) + 1,
        )