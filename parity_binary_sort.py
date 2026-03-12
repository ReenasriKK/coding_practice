def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        even_bits = []
        odd_bits = []
        
        for num in arr:
            if bin(num).count('1') % 2 == 0:
                even_bits.append(num)
            else:
                odd_bits.append(num)
        
        even_bits.sort()
        odd_bits.sort()
        
        result = even_bits + odd_bits
        print(*result)

solve()