import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

start = 0
end = int(houses[-1] - houses[0])

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    prev = houses[0]

    for house in houses:
        if house - prev >= mid:
            prev = house
            cnt += 1
        
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
print(end)
