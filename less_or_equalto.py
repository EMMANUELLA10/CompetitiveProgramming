t, n = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
if n == 0 and array[0] > 1:
    print(1)
elif n == 0 and array[0] == 1:
    print(-1)
elif n <= t-1:
    if array[n -1] != array[n]:
        print(array[n-1])
    else:
        print(-1)
elif n == t:
    print(array[n-1])