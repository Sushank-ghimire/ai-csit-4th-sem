% Autocrats are evils
evils(X) :-
  autocrat(X).

% Shyam is greedy leader
greedy(shyam).

% All greedy leaders are autocrat
autocrat(X) :-
  greedy(X).

% Gopal is a honest leader
honest(gopal).

% Query: Shyam is evils
%     evil(shyam).
