class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ''
        
        p_s = [0]*(len(shifts)+1)
        for i in range(len(shifts)-1,-1,-1):
            p_s[i]=p_s[i+1]+shifts[i]
        
        ord_a = ord('a')
        for i in range(len(shifts)):
            
            ans+=chr((ord(s[i]) - ord_a + p_s[i]) % 26 + ord_a)
            
        return ans