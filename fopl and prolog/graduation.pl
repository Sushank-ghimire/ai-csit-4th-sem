% Rinku is graduating
graduating(rinku).

% All people who are graduating are happy
happy(X) :-
  graduating(X).

% Happy people smiles
smiles(X) :-
  happy(X).

% Query : Is rinku smiles
%   smiles(rinku)
