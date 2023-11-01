def passenger_drive():
    global next_y, next_x, temp_move
    visited = [[-1] * (N + 1) for _ in range(N + 1)]
    temp_move = 500001

    if arr[start_y][start_x] == 2:
        next_y, next_x, temp_move = start_y, start_x, 0

    visited[start_y][start_x] = 0
    q = [(start_y, start_x)]
    while q:
        y, x = q.pop(0)
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ny, nx = y + dir[0], x + dir[1]
            if 1<=nx<=N and 1<=ny<=N:
                if arr[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                if arr[ny][nx] == 2:
                    if temp_move > visited[ny][nx]:
                        temp_move = visited[ny][nx]
                        next_y, next_x = ny, nx
                    elif temp_move == visited[ny][nx]:
                        if ny < next_y:
                            next_y, next_x, temp_move = ny, nx, visited[ny][nx]
                        elif ny == next_y:
                            if nx < next_x:
                                next_y, next_x, temp_move = ny, nx, visited[ny][nx]

def destination_drive():
    global start_y, start_x, temp_move
    visited = [[-1] * (N + 1) for _ in range(N + 1)]
    dest_y, dest_x = position[next_y][next_x]
    start_y, start_x = dest_y, dest_x
    visited[next_y][next_x] = 0
    temp_move = 500001
    q = [(next_y, next_x)]
    while q:
        y, x = q.pop(0)
        for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ny, nx = y + dir[0], x + dir[1]
            if 1 <= nx <= N and 1 <= ny <= N:
                if arr[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
                    if ny == dest_y and nx == dest_x:
                        temp_move = visited[ny][nx]
                        q = []
                        break

N, M, oil = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (N + 1)] + arr
position = [[0] * (N + 1) for _ in range(N + 1)]
start_y, start_x = map(int, input().split())
for _ in range(M):
    a, b, c, d = map(int, input().split())
    position[a][b] = (c, d)
    arr[a][b] = 2

temp_move = next_y = next_x = 0
passenger = M
while passenger != 0:

    passenger_drive()

    oil -= temp_move
    if oil <= 0:
        break

    arr[next_y][next_x] = 0

    destination_drive()

    if oil < temp_move:
        break

    oil += temp_move

    passenger -= 1

if passenger > 0:
    print(-1)
else:
    print(oil)