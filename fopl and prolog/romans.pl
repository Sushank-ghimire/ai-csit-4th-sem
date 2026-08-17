% All pompeian are romans
roman(X) :-
  pompeian(X).

% All romans were either loyal to caesar or hated him
loyal(X, caesar) :-
  roman(X).

hates(X, caesar) :-
  roman(X).

% Everyone is loyal to someone
someone(X) :-
  loyal(X).

% People only try to assassinate rulers they are not loyal to
assassinate(X, Y) :-
  not(loyal(X, Y)).

% Marcus tired to assassinate caesar
assassinate(marcus, caesar).

% Marcus was pompeian
pompeian(marcus).
