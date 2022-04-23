from scipy.optimize import linprog

# max z= x + y
# 2x + y <=20
# -4x + 5y <=10
# -x + 2y >=-2
# -x + 5y =15
# x,y>=0

obj = [1,1]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2]]  # Yellow constraint left side

rhs_ineq=[[20,10,2]]

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constrain

#bnd = [(0, float("inf")),  (0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf")), (0, float("inf"))]  # Bounds of y

bnd = [(0, float("inf")),  (0, float("inf"))]  # Bounds of y

opt =linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
               A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")
#opt =linprog(c=obj, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")

print(opt)