n, m = map(int, input().split())
r = [[i + 1] * m for i in range(n)]
for i in r:
    print(*i)
for i in range(n):
    for j in range(m):
        if i == j:
            r[i][j] = 0

print()
for i in r:
    print(*i)
s = 1
for i in range(n):
    for j in range(m):
        r[i][j] = s
        s += 1
print()
for i in r:
    print(*i)

r = [[0] * m for i in range(n)]
for i in range(n):
    s = 1
    for j in range(m):
        if j % 2 == 0:
            continue
        r[i][j] = s
        s += 1
print()
for i in r:
    print(*i)