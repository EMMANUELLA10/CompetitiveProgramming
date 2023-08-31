class Solution(object):
    p_sum =[]
    po_sum=[] 
    def productExceptSelf(self, nums):
        self.p_sum = [0]*(len(nums))
        self.po_sum =[0]*(len(nums))
        
        answer = []
        self.p_sum[0]=1
        for i in range(0,len(nums)-1):
            self.p_sum[i+1]=nums[i]*self.p_sum[i]
    

        self.po_sum[len(nums)-1]=1
        for i in range(len(nums)-1,0,-1):
            self.po_sum[i-1]=nums[i]*self.po_sum[i]
        
        print(self.po_sum,self.p_sum)

        for i in range(len(nums)):
            answer.append(self.p_sum[i]*self.po_sum[i])

        return answer