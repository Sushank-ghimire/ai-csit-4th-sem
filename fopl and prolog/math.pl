% HCF (Highest Common Factor) usong Euclidean algorithm

hcf(A, B, H) :-
  A > B,
  R is B mod A,
  hcf(B, R, H).

hcf(A, B, H) :-
  A < B,
  R is B mod A,
  hcf(A, R, H).

hcf(A, B, A) :-
  A =:= B.

% LCM (Least Common Multiple)

lcm(A, B, L) :-
  hcf(A, B, H),
  L is (A * B) // H.

% Cube
cube :-
  write('Enter a number: '),
  read(N),
  C is N * N * N,
  write('Cube of the number is: '),
  write(C).

% Sum
sum :-
  write('Enter first number: '),
  read(A),
  write('Enter second number: '),
  read(B),
  S is A + B,
  write('Sum is: '),
  write(S).

% Difference
difference :-
  write('Enter first number: '),
  read(A),
  write('Enter second number: '),
  read(B),
  D is A - B,
  write('Difference is: '),
  write(D).


% Divide
divide :-
  write('Enter first number: '),
  read(A),
  write('Enter second number: '),
  read(B),
  D is A / B,
  write('Division of first/second is: '),
  write(D).
