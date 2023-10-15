# 인구 이동이 며칠 동안 발생하는지
# N : 땅의 크기, L, R : 인구 차이가 L명 이상 R명 이하
N, L, R = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]

# 인구 이동이 발생한 날을 셀 변수
cnt = 0

# 상우하좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move_people(y, x):
    pos = [(y, x)]
    people = [space[y][x]]
    q = [(y, x)]
    while q:
        sy, sx = q.pop(0)
        for d in dir:
            ny, nx = sy + d[0], sx + d[1]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == 1 and L <= abs(space[sy][sx] - space[ny][nx]) <= R:
                    pos.append((ny, nx))
                    people.append(space[ny][nx])
                    visited[ny][nx] = 0
                    q.append((ny, nx))

    if len(pos) > 1:
        avg = int(sum(people)/len(pos))
        for p in pos:
            space[p[0]][p[1]] = avg
        return True
    else: return False

while True:
    check = False
    visited = [[1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                visited[i][j] = 0
                if not check:
                    check = move_people(i, j)
                else: move_people(i, j)
    if check:
        cnt += 1
    else:
        print(cnt)
        break