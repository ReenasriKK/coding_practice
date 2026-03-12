t = int(input())

for _ in range(t):
    g, p = map(int, input().split())
    n = int(input())
    
    prob1 = 0
    prob2 = 0
    
    for _ in range(n):
        a, b = map(int, input().split())
        prob1 += a
        prob2 += b
    
    cost1 = prob1 * g + prob2 * p
    cost2 = prob1 * p + prob2 * g
    
    print(min(cost1, cost2))