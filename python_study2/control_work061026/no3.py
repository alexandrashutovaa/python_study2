M, N = map(int, input().split())
str_arr = [input() for _ in range(N)]
x, y, d = map(int, input().split())

for row in range(max(0, y - d), min(N, y + d + 1)):
    print(str_arr[row][max(0, x - d) : min(M, x + d + 1)])
