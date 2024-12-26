% 基本图形关系
point_on_line(P, L) :-
    line(L),
    point(P),
    endpoints(L, P1, P2),
    collinear(P, P1, P2).

collinear(P1, P2, P3) :-
    coordinates(P1, X1, Y1),
    coordinates(P2, X2, Y2),
    coordinates(P3, X3, Y3),
    % 使用向量叉积判断三点共线
    (X2 - X1) * (Y3 - Y1) =:= (X3 - X1) * (Y2 - Y1).