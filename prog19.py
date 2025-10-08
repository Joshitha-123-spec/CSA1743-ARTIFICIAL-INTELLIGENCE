graph={'S':{'A':1,'B':4},'A':{'B':2,'C':5},'B':{'C':1},'C':{}}
heuristic={'S':7,'A':6,'B':2,'C':0}

def a_star(start,goal):
    open_set={start}; g={start:0}; f={start:g[start]+heuristic[start]}; parent={}
    while open_set:
        current=min(open_set,key=lambda x:f[x])
        if current==goal:
            path=[current]
            while current in parent:
                current=parent[current]; path.append(current)
            print("Path:",path[::-1]); return
        open_set.remove(current)
        for n in graph[current]:
            t=g[current]+graph[current][n]
            if n not in g or t<g[n]:
                g[n]=t; f[n]=t+heuristic[n]; parent[n]=current
                open_set.add(n)

a_star('S','C')
