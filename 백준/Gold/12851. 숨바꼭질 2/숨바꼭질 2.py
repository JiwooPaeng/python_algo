from collections import deque
N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100002)]
visited[N][0] = 0 # 해당 숫자에 도착할때까지 걸린 시간
visited[N][1] = 1 # 해당 숫자까지 도착하는데 걸린 경우의 수

route = 0
q = deque()
q.append(N)
while q:
    num = q.popleft()

    for move in [num-1, num+1, 2*num]:
        if 0 <= move <= 100001:
            if visited[move][0] == -1: # 처음 방문하는 경우
                visited[move][0] = visited[num][0] + 1 # 출발노드의 걸린시간 + 1
                visited[move][1] = visited[num][1] # 처음 방문하는 경우이기 때문에 경우의 수에 변화 없다
                q.append(move)
            # 방문 했던 곳을 다시 방문하는 경우
            elif visited[move][0] == visited[num][0] + 1:
                visited[move][1] += visited[num][1] # 경우의 수를 합산해준다

print(visited[K][0])
print(visited[K][1])