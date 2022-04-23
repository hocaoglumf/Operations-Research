from scipy.optimize import linprog

# max z= x + y
# 2x + y <=20
# -4x + 5 <=10
# -x + 2y >=-2
# -x + 5y =15
# x,y>=0

obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2],
            [-1, 5],
            [1, -5]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
             10,  # Blue constraint right side
              2, 15,-15]  # Yellow constraint right side


bnd = [(0, float("inf")),  # Bounds of x
 (0, float("inf"))]  # Bounds of y

opt =linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
               bounds=bnd,
               method="revised simplex")
print(opt)

obj2=[388, 235, 784, 272, 388, 153, 1154, 486, 235, 153, 1054, 3346, 784, 1154, 1054, 841,
272, 486, 334, 841]

for i in range(1,5):
    for j in range(1,5):
        print("x"+str(i)+","+str(j))
