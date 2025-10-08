% --- Tower of Hanoi Program ---
% move(N, From, To, Aux) means: move N disks from From to To using Aux as helper.

move(1, From, To, _) :-
    write('Move the top disk from '), write(From), write(' to '), write(To), nl.

move(N, From, To, Aux) :-
    N > 1,
    M is N - 1,
    move(M, From, Aux, To),
    move(1, From, To, _),
    move(M, Aux, To, From).