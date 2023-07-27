class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1, len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            count = sum(1 for n in nums if l <= n <= mid)
            totalNums = mid - l + 1
            if count > totalNums:
                r = mid
            else:
                l = mid + 1

        return l



        