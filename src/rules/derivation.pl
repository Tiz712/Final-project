% 规则推导系统
derive(InitialFacts, Goal, Proof) :-
    derive_step(InitialFacts, [], Goal, RevProof),
    reverse(RevProof, Proof).

derive_step(Facts, Proof, Goal, FinalProof) :-
    member(Goal, Facts),  % 目标已经在事实集中
    append(Proof, [goal_reached(Goal)], FinalProof).

derive_step(Facts, Proof, Goal, FinalProof) :-
    select_rule(Rule),    % 选择适用的规则
    apply_rule(Rule, Facts, NewFact),
    \+ member(NewFact, Facts),
    append(Facts, [NewFact], NewFacts),
    append(Proof, [applied_rule(Rule, NewFact)], NewProof),
    derive_step(NewFacts, NewProof, Goal, FinalProof).