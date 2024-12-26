% 1. 连接公理：两点确定一条直线
axiom_connect(P1, P2, L) :-
    point(P1), point(P2),
    P1 \= P2,
    construct_line(P1, P2, L).

% 2. 延长公理：直线可以无限延长
axiom_extend(L, P, ExtL) :-
    line(L),
    point(P),
    point_on_line(P, L),
    extend_line(L, P, ExtL).

% 3. 圆公理：给定圆心和半径可以作圆
axiom_circle(Center, Radius, C) :-
    point(Center),
    number(Radius),
    Radius > 0,
    construct_circle(Center, Radius, C).

% 4. 全等公理：三角形全等的基本条件
axiom_congruence(T1, T2) :-
    triangle(T1), triangle(T2),
    (sas_condition(T1, T2);    % 边角边
     asa_condition(T1, T2);    % 角边角
     sss_condition(T1, T2)).   % 三边相等

% 5. 平行公理：过直线外一点有唯一平行线
axiom_parallel(P, L, PL) :-
    point(P),
    line(L),
    not(point_on_line(P, L)),
    construct_parallel(P, L, PL).