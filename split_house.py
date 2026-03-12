n = int(input())
s = input()

if 'H' not in s:
    print("NO")
else:
    result = ""
    for ch in s:
        if ch == '.':
            result += 'B'
        else:
            result += 'H'
    
    print("YES")
    print(result)