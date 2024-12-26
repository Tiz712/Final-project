% Basic geometric elements
point(P) :- coordinates(P, _, _).
line(L) :- endpoints(L, _, _).
circle(C) :- center(C, P), radius(C, R).
angle(A) :- vertex(A, V), ray1(A, R1), ray2(A, R2).

% Basic geometric relations
collinear(P1, P2, P3) :-
    coordinates(P1, X1, Y1),
    coordinates(P2, X2, Y2),
    coordinates(P3, X3, Y3),
    (X2 - X1) * (Y3 - Y1) =:= (X3 - X1) * (Y2 - Y1).

distance(P1, P2, D) :-
    coordinates(P1, X1, Y1),
    coordinates(P2, X2, Y2),
    D is sqrt((X2-X1)^2 + (Y2-Y1)^2).

% Basic axioms
axiom_connect(P1, P2, L) :-
    point(P1), point(P2),
    P1 \= P2,
    construct_line(P1, P2, L).

axiom_circle(Center, Radius, C) :-
    point(Center),
    number(Radius),
    Radius > 0,
    construct_circle(Center, Radius, C).