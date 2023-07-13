def merge_sorted_arrays(n, m, arr1, arr2):
    merged = []
    i = 0
    j = 0
    
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    while i < n:
        merged.append(arr1[i])
        i += 1
    
    while j < m:
        merged.append(arr2[j])
        j += 1
    
    return merged


# Read input
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Merge the sorted arrays
result = merge_sorted_arrays(n, m, arr1, arr2)

# Print the merged array
for num in result:
    print(num, end=" ")
