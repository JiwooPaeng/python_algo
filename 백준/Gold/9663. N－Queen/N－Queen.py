def queens(curr):
    global ans
    if curr == N:
        ans += 1
        return

    for i in range(N):
        if not visited[i] and not left_diag[curr-i] and not right_diag[curr+i]:
            boards[curr] = i
            visited[i] = left_diag[curr-i] = right_diag[curr+i] = 1
            queens(curr + 1)
            visited[i] = left_diag[curr-i] = right_diag[curr+i] = 0

N = int(input())
boards = [0 for _ in range(N)]
visited = [0 for _ in range(N)]
left_diag = [0 for _ in range(2*N-1)]
right_diag = [0 for _ in range(2*N-1)]
ans = 0
queens(0)

print(ans)