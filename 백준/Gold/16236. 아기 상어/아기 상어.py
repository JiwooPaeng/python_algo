def fish_fish(next, shark):
    global sy, sx, fish_min
    while next:
        y, x = next.popleft()
        for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  
            ny, nx = y + dir[0], x + dir[1]
            if 0 <= ny <= N - 1 and 0 <= nx <= N - 1 and arr[ny][nx] <= shark[0]:
                if not distance[ny][nx] :
                    distance[ny][nx] = distance[y][x] + 1
                    next.append((ny, nx))
                if arr[ny][nx] != 0 and arr[ny][nx] < shark[0]:
                    if distance[ny][nx] < fish_min:
                        fish_min = distance[ny][nx]
                        sy, sx = ny, nx
                    elif distance[ny][nx] == fish_min:
                        if ny < sy:
                            sy, sx = ny, nx
                        elif ny == sy:
                            if nx < sx:
                                sx = nx

from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = -1 
sy = sx = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt += 1
        if arr[i][j] == 9:
            sy, sx = i, j
            arr[i][j] = 0
shark = [2, 0]
total = 0
while cnt != 0:
    distance = [[0] * N for _ in range(N)]
    distance[sy][sx] = 1
    next = deque()
    next.append((sy, sx))
    fish_min = N * N + 1
    fish_fish(next, shark, )

    if fish_min == N * N + 1 :
        break

    arr[sy][sx] = 0
    shark[1] += 1

    if shark[1] == shark[0]:
        shark[0] += 1
        shark[1] = 0

    total += distance[sy][sx] - 1

    cnt -= 1

print(total)