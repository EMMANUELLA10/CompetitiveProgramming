class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        container = {}
        start = 0
        for i in range(len(nums)):
            if nums[i] in container:
                start += container[nums[i]]
                container[nums[i]] +=1
            else:
                container[nums[i]] = 1
        return start