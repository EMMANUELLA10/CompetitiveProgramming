n = int(input())

array = list(map(int, input().split()))

even_count, odd_count = 0,0

for i in range(n):
    if array[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > 0 and odd_count > 0:
    array.sort()

print(*array)