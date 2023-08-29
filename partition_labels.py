class Solution:
    def partitionLabels(self, s: str):
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end=max(end, s.rindex(s[i]))
            if i==end:
                res.append(end-start+1)
                start=i+1

        return res
            