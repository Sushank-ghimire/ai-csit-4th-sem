% Base cases

fib(0, 0).
fib(1, 1).

% Recursive Case
fib(N, F):-
  N > 1,
  N1 is N - 1,
  N2 is N - 2,
  fib(N1, F1),
  fib(N2, F2),
  F is F1 + F2.

% Print fibonacci series up to N terms
print_fib(0).
print_fib(N) :-
  N > 0,
  N1 is N - 1,
  print_fib(N1),
  fib(N1, F),
  write(F), write(' ').
