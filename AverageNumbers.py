n = int(input())
def solve(a):
    n = len(a)
    num_sum = sum(a)
    ans = []
    for  i in range(n): 
        if  (num_sum-a[i])==a[i]*n-a[i]:
            ans.append(i+1)
    print(len(ans))
    print(*ans)

a = list(map(int, input().split()))
solve(a)