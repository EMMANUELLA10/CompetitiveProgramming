t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    
 
    for x in range(2):
        res = n - x * k
        if  res >= 0 and res % 2 == 0:
            print("YES")
            break
 
    else:
        print("NO")