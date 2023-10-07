# input 받아오기
N = int(input())
# data = [list(input().split()) for _ in range(N)]
data = []
for _ in range(N):
    data.append(list(map(int, input())))

# 탐색하기
# 방향 설정 (상우하좌)
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 단지 수
num = 0
# 단지 별 집 수
blocks = []

def countBlock(start, blocks):
    count = 1
    data[start[0]][start[1]] = 0
    q = [start]
    while q:
        di, dj = q.pop(0)
        for d in dir:
            dy, dx = di + d[0], dj + d[1]
            if N > dx >= 0 and N > dy >= 0:
                if data[dy][dx] == 1:
                    q.append((dy, dx))
                    count += 1
                    data[dy][dx] = 0

    blocks.append(count)

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            num += 1
            countBlock((i, j), blocks)

print(num)
blocks.sort()
for i in range(num):
    print(blocks[i])