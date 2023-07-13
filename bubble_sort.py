def countSwaps(a):
    count=0
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j+1],a[j]
                count+=1
    return f"Array is sorted in {count} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}"

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(countSwaps(a))