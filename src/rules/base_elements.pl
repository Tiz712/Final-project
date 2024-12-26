% 基础图形元素定义
point(P) :- coordinates(P, _, _).
line(L) :- endpoints(L, _, _).
circle(C) :- center(C, P), radius(C, R).
angle(A) :- vertex(A, V), ray1(A, R1), ray2(A, R2).

% 基本度量关系
distance(P1, P2, D) :-
    coordinates(P1, X1, Y1),
    coordinates(P2, X2, Y2),
    D is sqrt((X2-X1)^2 + (Y2-Y1)^2).

angle_measure(A, M) :-
    angle(A),
    vertex(A, V),
    ray1(A, R1),
    ray2(A, R2),
    calculate_angle(V, R1, R2, M).