class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        return bisect_left(nums, target)