import copy

arr = [list(map(int, input().split())) for _ in range(4)]

space = []
for i in range(4):
    list = []
    for j in range(4):
        list.append([arr[i][2*j], arr[i][2*j + 1] - 1])
    space.append(list)

dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# 물고기 번호 합의 최댓값 찾기
def bite_fish(shark, temp_bite, sites):
    global max_bite

    if max_bite < temp_bite:
        max_bite = temp_bite
    temp_sites = copy.deepcopy(sites)

    # 물고기들 이동 시작
    for i in range(1, 17):
        cy, cx = -1, -1
        for y in range(4):
            for x in range(4):
                if temp_sites[y][x][0] == i:
                    cy, cx = y, x
                    break
        if cy == -1 or cx == -1:
            continue
        cd = temp_sites[cy][cx][1]

        for j in range(8):
            nd = (cd+j) % 8
            ny, nx = cy + dir[nd][0], cx + dir[nd][1]
            if (ny > 3 or ny < 0 or nx > 3 or nx < 0) or (shark[0][0] == ny and shark[0][1] == nx):
                continue
            temp_sites[cy][cx][1] = nd
            temp_sites[cy][cx], temp_sites[ny][nx] = temp_sites[ny][nx], temp_sites[cy][cx]
            break

    # 물고기의 이동이 끝나고, 상어가 먹이를 먹을 차례
    n = 1
    # 이전 상어의 위치
    sy, sx = shark[0][0], shark[0][1]
    # 상어가 먹을 수 있는 물고기 모두 찾기
    while True:
        # 상어가 이동할 것을 예상되는 좌표
        ny, nx = sy + dir[temp_sites[sy][sx][1]][0] * n,  sx + dir[temp_sites[sy][sx][1]][1] * n
        # 좌표가 영역 밖으로 넘어갈 경우, break
        if ny < 0 or ny > 3 or nx < 0 or nx > 3:
            break
        # 상어가 먹이를 먹으러 해당 위치로 이동할 수 있는 경우
        if temp_sites[ny][nx][0] > 0:
            # 상어가 이동 후 다음 시행 시작
            shark = [(ny, nx), temp_sites[ny][nx][1]]
            temp_num = temp_sites[ny][nx][0]
            temp_sites[ny][nx][0] = 0
            bite_fish(shark, temp_bite+temp_num, temp_sites)
            temp_sites[ny][nx][0] = temp_num

        n += 1
        # 상어가 이동 가능한 칸이 없으면 자동으로 종료됨

# 시작점, 상어 위치와 방향 index
shark = [(0, 0), space[0][0][1]]

max_bite = 0
temp_bite = space[0][0][0]
space[0][0][0] = 0
bite_fish(shark, temp_bite, space)

print(max_bite)