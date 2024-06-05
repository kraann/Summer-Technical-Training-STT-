T = int(input())

for _ in range(T):
    
    N, K = map(int, input().split())
    
    A = list(map(int, input().split()))
    
    min_value = min(A)
    
    time_needed = max(0, K - min_value)
    
    print(time_needed)
