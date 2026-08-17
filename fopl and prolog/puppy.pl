% Puppy is a dog.
dog(puppy).

% All dogs are animals.
animal(X) :-
    dog(X).

% All animals die.
die(X) :-
    animal(X).


% Query:
%   die(puppy).
