# N개 행, M개 열
N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]

# 상우하좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 구역의 개수 담을 변수
sections = 0
def search_section(y, x):
    q = [(y, x)]
    while q:
        ty, tx = q.pop(0)
        for d in dir:
            # 영역을 넘어가는 경우 순회
            cy, cx = ty + d[0], tx + d[1]
            if cy < 0 or cy > N - 1:
                cy = cy % N
            if cx < 0 or cx > M - 1:
                cx = cx % M
            if not planet[cy][cx]:
                planet[cy][cx] = 1
                q.append((cy, cx))

for i in range(N):
    for j in range(M):
        # 아직 구역 탐색 되지 않은 경우, 구역 탐색
        if not planet[i][j]:
            sections += 1
            planet[i][j] = 1
            search_section(i, j)
print(sections)