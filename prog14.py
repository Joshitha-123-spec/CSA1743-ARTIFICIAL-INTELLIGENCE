from collections import deque
def valid(m,c): return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)
def bfs():
    start=(3,3,1);goal=(0,0,0)
    q=deque([start]);vis=set()
    while q:
        m,c,b=q.popleft()
        if (m,c,b)==goal: print("Goal");return
        if (m,c,b) in vis: continue
        vis.add((m,c,b))
        for dm,dc in [(1,0),(0,1),(1,1),(2,0),(0,2)]:
            if b: nm,nc,nb=m-dm,c-dc,0
            else: nm,nc,nb=m+dm,c+dc,1
            if 0<=nm<=3 and 0<=nc<=3 and valid(nm,nc):
                q.append((nm,nc,nb))
bfs()
