% Facts
% Horses are mammals.
mammal(horse).

% Cows are mammals.
mammal(cows).

% Pigs are mammals.
mammal(pig).

% Bluebeard is a horse.
horse(bluebeard).

% Bluebeard is charlie's parent.
parent(bluebeard, charlie).

% Rules or Constraints
% An offspring of a horse is also a horse
% If X is a horse and X is the parent of Y, then Y is horse
horse(Y) :-
  horse(X),
  parent(X, Y).

% Offspring and parent are inverse relations.
% If X is the parent of Y, then Y is the offspring of X.
offspring(Y, X) :-
  parent(X, Y).

% If X is the offspring of Y, then Y is the parent of X.
parent(Y, X) :-
  offspring(X, Y).

% Every mammal has a parent
% Every mammal has a parent i.e if X is a mammal then X has a parent.
has_parent(X) :-
  mammal(X).

% Query:
% ?- horse(charlie).

% Step 1:
% We know that Bluebeard is a horse.
%
% horse(bluebeard).
%
% Step 2:
% We know that Bluebeard is Charlie's parent.
%
% parent(bluebeard, charlie).
%
% Step 3:
% We have the rule:
%
% horse(Y) :-
%     horse(X),
%     parent(X, Y).
%
% This means:
% If X is a horse AND X is the parent of Y,
% then Y is a horse.
%
% Step 4:
% Prolog matches:
%
% X = bluebeard
% Y = charlie
%
% because:
%
% horse(bluebeard).
% parent(bluebeard, charlie).
%
% Step 5:
% Therefore:
%
% horse(charlie).
%
% So the answer to the query is YES.
