% 8 Queens Problem

% Main predicate
queens(Solution) :-
    Solution = [A,B,C,D,E,F,G,H],
    permutation([1,2,3,4,5,6,7,8], Solution),
    safe(Solution).

% Check that all queens are safe
safe([]).

safe([Queen|Rest]) :-
    check(Queen, Rest, 1),
    safe(Rest).

% Check one queen with the remaining queens
check(_, [], _).

check(Queen, [Next|Rest], Distance) :-
    Queen =\= Next,
    abs(Queen - Next) =\= Distance,
    NewDistance is Distance + 1,
    check(Queen, Rest, NewDistance).
