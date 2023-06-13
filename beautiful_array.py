n = int(input())
numbers = list(map(int, input().split()))
less_than_zero =  []
equal_to_zero = []
greater_than_zero =  []
for i in range(len(numbers)):
    if numbers[i] < 0:
        less_than_zero.append(numbers[i])
    elif numbers[i] == 0:
        equal_to_zero.append(numbers[i])
    else:
        greater_than_zero.append(numbers[i])
if not greater_than_zero:
    greater_than_zero.append(less_than_zero.pop())
    greater_than_zero.append(less_than_zero.pop())
if not len(less_than_zero)%2:
    equal_to_zero.append(less_than_zero.pop())

print(len(less_than_zero), *less_than_zero)
print(len(greater_than_zero), *greater_than_zero)
print(len(equal_to_zero), *equal_to_zero)