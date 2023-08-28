class Solution:
    def twoSum(self, numbers, target):
        index1 = 0
        index2 = len(numbers) - 1

        while index1 < index2:
           sum = numbers[index1] + numbers[index2]
           if sum == target:
              return [index1 + 1, index2 + 1]
           elif sum < target:
              index1 += 1
           else:
              index2 -= 1
    
    
        return []
