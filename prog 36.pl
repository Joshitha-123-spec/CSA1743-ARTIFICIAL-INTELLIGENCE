% Graph edges
edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 3).
edge(c, d, 1).
edge(c, e, 5).
edge(d, f, 2).
edge(e, f, 1).

% Heuristic values (estimated cost to goal)
h(a, 6).
h(b, 4).
h(c, 2).
h(d, 1).
h(e, 3).
h(f, 0).

% Best-First Search
bestfs(Start, Goal, Path) :- 
    bestfs_search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

bestfs_search([[Goal|Rest]|_], Goal, [Goal|Rest]).
bestfs_search([ [Node|Path] | Paths], Goal, FinalPath) :-
    findall([Next, Node|Path],
            (edge(Node, Next, _), \+ member(Next, [Node|Path])),
            NewPaths),
    add_heuristic(NewPaths, Scored),
    append(Paths, Scored, AllPaths),
    sort_paths(AllPaths, Sorted),
    bestfs_search(Sorted, Goal, FinalPath).

add_heuristic([], []).
add_heuristic([[N|_]=P|Rest], [[H-N|P]|Tail]) :-
    h(N, H),
    add_heuristic(Rest, Tail).

sort_paths(Paths, Sorted) :-
    sort(Paths, Sorted).
