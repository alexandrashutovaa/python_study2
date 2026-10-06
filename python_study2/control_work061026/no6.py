N = int(input())
sensors = {}
for _ in range(N):
    name, val = input().split()
    if name in sensors:
        sensors[name].append(int(val))
    else:
        sensors[name] = [int(val)]

M = int(input())
for _ in range(M):
    name = input()
    if name not in sensors:
        print("no data")
    else:
        vals = sorted(sensors[name])
        print(vals[(len(vals) - 1) // 2])