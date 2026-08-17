% American, Weapons & Criminals

% Facts
% George is an American.
american(george).

% Iraq is a country.
country(iraq).

% Iraq is an enemy of America.
enemy(iraq, america).

% Iraq has missiles.
has(iraq, missiles).

% All missiles of Iraq were sold by George.
sold(george, missiles, iraq).

% Missiles are weapons.
weapon(missiles).

% Rules or Constraints
% Every enemy of America is hostile.
% If X is an enemy of America, then X is hostile.
hostile(X) :-
    enemy(X, america).

% Every American who sells weapons to hostile nations is a criminal.
% If X is an American, X sells a weapon to Y, and Y is hostile, then X is a criminal.
criminal(X) :-
    american(X),
    sold(X, Weapon, Y),
    weapon(Weapon),
    hostile(Y).

% Query:
% ?- criminal(george).

% Prolog substitutes:
% X = george
% Weapon = missiles
% Y = iraq
%
% And checks:
% american(george)       -> TRUE
% sold(george, missiles, iraq) -> TRUE
% weapon(missiles)       -> TRUE
% hostile(iraq)          -> TRUE

% Therefore:
% criminal(george)
% is TRUE.
