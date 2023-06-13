class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        for i in range(m+n):
            if i < m:
                nums1[i] = nums1[i]
            else:
                nums1[i] = nums2[i-m]
        nums1.sort()
            
ans = Solution()
ans.merge([1,2,4,0,3,1],3,[2,7,6],3)