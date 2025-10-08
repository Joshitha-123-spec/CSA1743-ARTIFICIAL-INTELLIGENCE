colors=['Red','Green','Blue']
graph={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
assignment={}
def safe(node,color):
    for n in graph[node]:
        if assignment.get(n)==color: return False
    return True

def solve(nodes):
    if not nodes: print(assignment); return True
    node=nodes[0]
    for c in colors:
        if safe(node,c):
            assignment[node]=c
            if solve(nodes[1:]): return True
            assignment.pop(node)
solve(list(graph.keys()))
