class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rowstart = 0
        rowend = len(matrix)
        colstart = 0
        colend = len(matrix[0])
        res = []

        if not matrix:
            return 0

        while rowstart < rowend and colstart < colend:
            for i in range(colstart, colend):
                res.append(matrix[rowstart][i])
            for j in range(rowstart+1, rowend-1):
                res.append(matrix[j][colend-1])

            if rowend != rowstart+1:
                for i in range(colend-1, colstart-1, -1):
                    res.append(matrix[rowend-1][i])
            if colend != colstart+1:
                for j in range(rowend-2, rowstart, -1):
                    res.append(matrix[j][colstart])
            rowstart += 1
            rowend -= 1
            colstart += 1
            colend -= 1

        return res