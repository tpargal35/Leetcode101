def minOperations(s: str) -> int:
    c = 0
    for i in range(len(s)):
        if s[i] == ('0' if i % 2 == 0 else '1'):
            c += 1
    return min(c, len(s) - c)

print(minOperations('1011'))  