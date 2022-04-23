
:-consult(tree).

parent(s, o1).
cost(s,0).
profit(s,0).

cost(o1,0).
profit(o1,0).

parent(s, o2).

cost(o2,4000).
profit(o2,8000).

parent(s, o3).
cost(o3,6000).
profit(o3,10000).

parent(o1,o1b1).
cost(o1b1,0).
profit(o1b1,0).

parent(o1,o1b2).
cost(o1b2,8000).
profit(o1b2,12000).

parent(o1,o1b3).
cost(o1b3,12000).
profit(o1b3,18000).

parent(o2,o2b1).
cost(o2b1,0).
profit(o2b1,0).

parent(o2,o2b2).
cost(o2b2,8000).
profit(o2b2,12000).

parent(o2,o2b3).
cost(o2b3,12000).
profit(o2b3,18000).

parent(o3,o3b1).
cost(o3b1,0).
profit(o3b1,0).

parent(o3,o3b2).
cost(o3b2,8000).
profit(o3b2,12000).

parent(o3,o3b3).
cost(o3b3,12000).
profit(o3b3,18000).


parent(o1b1,d1).
parent(o1b1,d2).
cost(d1,0).
cost(d2,2000).
profit(d1,0).
profit(d2,8000).

parent(o1b2,d3).
parent(o1b2,d4).
cost(d3,0).
cost(d4,2000).
profit(d3,0).
profit(d4,8000).

parent(o1b3,d5).
parent(o1b3,d6).
cost(d5,0).
cost(d6,2000).
profit(d5,0).
profit(d6,8000).


parent(o2b1,d7).
parent(o2b1,d8).
cost(d7,0).
cost(d8,2000).
profit(d7,0).
profit(d8,8000).

parent(o2b2,d9).
parent(o2b2,d10).
cost(d9,0).
cost(d10,2000).
profit(d9,0).
profit(d10,8000).

parent(o2b3,d11).
parent(o2b3,d12).
cost(d11,0).
cost(d12,2000).
profit(d11,0).
profit(d12,8000).

parent(o3b1,d13).
parent(o3b1,d14).
cost(d13,0).
cost(d14,2000).
profit(d13,0).
profit(d14,8000).


parent(o3b2,d15).
parent(o3b2,d16).
cost(d15,0).
cost(d16,2000).
profit(d15,0).
profit(d16,8000).

parent(o3b3,d17).
parent(o3b3,d18).
cost(d17,0).
cost(d18,2000).
profit(d17,0).
profit(d18,8000).







