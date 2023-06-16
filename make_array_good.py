for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    array_copy = array.copy()
    array.sort()
    operations = []
    
    for i in range(1,n):
        idx = array_copy.index(array[i])
        remainder = (array[i - 1] - (array[i] % array[i - 1])) % array[i - 1]
        array[i] += remainder
        if remainder:
            operations.append((idx+1, remainder))
        array_copy[idx] = -1
    print(len(operations))
    for i in operations:
        print(*i)