class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_h = sorted(heights)[::-1]
        indices = []
        for i in new_h:
            indices.append(heights.index(i))
        result = [names[i] for i in indices]
        return result