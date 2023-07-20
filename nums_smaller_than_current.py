class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        ans = sorted(nums)
        hashmap = defaultdict(int)
        
        for i in range(len(ans)-1,-1,-1):
            hashmap[ans[i]] = i
            
        for i in range(len(nums)):
            nums[i] = hashmap[nums[i]]
            
        return nums