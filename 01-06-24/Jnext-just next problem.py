t = int(input())

for _ in range(t):
    n = int(input())
    
    digits = list(map(int, input().split()))
    
    pivot_index = -1
    for i in range(n - 1, 0, -1):
        if digits[i] > digits[i - 1]:
            pivot_index = i - 1
            break
    
    if pivot_index == -1:
        print(-1)
        continue
    
    smallest_greater_index = pivot_index + 1
    for i in range(pivot_index + 1, n):
        if digits[i] > digits[pivot_index] and digits[i] < digits[smallest_greater_index]:
            smallest_greater_index = i
    
    digits[pivot_index], digits[smallest_greater_index] = digits[smallest_greater_index], digits[pivot_index]
    
    digits[pivot_index + 1:] = sorted(digits[pivot_index + 1:])

    next_greater = ''.join(map(str, digits))
    print(next_greater)
