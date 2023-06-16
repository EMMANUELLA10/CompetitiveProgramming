s = ["h","e","l","l","o"]

n=list(s)
s.clear()
print(n)
for i in range(len(n)-1,-1,-1):
    s.append(n[i])
    
print(s)