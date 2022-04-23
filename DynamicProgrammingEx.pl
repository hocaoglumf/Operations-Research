c(1,2,10).
c(1,3,15).
c(1,4,20).

c(2,1,5).
c(2,3,9).
c(2,4,10).

c(3,1,6).
c(3,2,13).
c(3,4,12).

c(4,1,8).
c(4,2,8).
c(4,3,9).

all_possible_paths(CityA, CityB) :-
    write(CityA),
    nl,
    loop_process(CityA, CityB).

loop_process(CityA, CityB) :- 
    CityA == CityB.
loop_process(CityA, CityB) :-
    CityA \== CityB,
    c(CityA, X, _),
    write(X),
    nl,
    loop_process(X, CityB).



