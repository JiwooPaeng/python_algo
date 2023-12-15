N = int(input())
arr = [[] for _ in range(N)]
for _ in range(N):
    p, c = map(int, input().split())
    arr[c - 1].append(p)
ans = 0
for color in arr:
    color.sort()
    if len(color) > 1:
        ans += (color[1] - color[0]) + (color[-1] - color[-2])
        for i in range(1, len(color) - 1):
            ans += min((color[i] - color[i - 1]), (color[i + 1] - color[i]))
print(ans)