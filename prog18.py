from itertools import permutations

dist = {('A','B'):10,('A','C'):15,('A','D'):20,
        ('B','A'):10,('B','C'):35,('B','D'):25,
        ('C','A'):15,('C','B'):35,('C','D'):30,
        ('D','A'):20,('D','B'):25,('D','C'):30}

cities=['A','B','C','D']
min_dist=float('inf'); min_path=None

for perm in permutations(cities[1:]):
    path=['A']+list(perm)+['A']
    d=sum(dist[(path[i],path[i+1])] for i in range(len(path)-1))
    if d<min_dist: min_dist=d; min_path=path

print("Shortest Path:",min_path)
print("Distance:",min_dist)
