% All oversmart persons are stupid
stupid(X) :-
    oversmart(X).

% Children of all stupid persons are naughty
naughty(X) :-
    child(X, Y),
    stupid(Y).

% Ram is the child of Hari
child(ram, hari).

% Hari is oversmart
oversmart(hari).
