vs = list(map(int, input().split()))
neighbors = {}
for v in vs:
    neighbors[v] = set()

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    neighbors[a].add(b)
    neighbors[b].add(a)

starts = list(map(int, input().split()))

result = set()
for s in starts:
    result.add(s)
    for nb in neighbors[s]:
        result.add(nb)

for v in sorted(result):
    print(v, end=' ')
print()