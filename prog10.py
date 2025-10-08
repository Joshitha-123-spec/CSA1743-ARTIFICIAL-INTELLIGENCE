from collections import deque

def bfs(start, goal):
    q = deque([start])
    visited = {tuple(start): None}
    while q:
        state = q.popleft()
        if state == goal: break
        i = state.index(0)
        x,y = divmod(i,3)
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<3 and 0<=ny<3:
                new = state[:]
                j = nx*3+ny
                new[i],new[j] = new[j],new[i]
                if tuple(new) not in visited:
                    visited[tuple(new)] = state
                    q.append(new)
    return visited

start=[1,2,3,4,0,5,6,7,8]
goal=[1,2,3,4,5,6,7,8,0]
visited = bfs(start,goal)
print("Solved:",goal)
