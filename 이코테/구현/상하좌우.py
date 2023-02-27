n = int(input())
x,y = 1, 1
plans = input().split()

# up, right, down, left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move_types = ['U', 'R', 'D', 'L']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)