def commonChars(self,A):
        check = list(A[0])
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check