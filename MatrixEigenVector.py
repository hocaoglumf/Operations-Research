import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la


#M=[[-2,0,0],[0,-2,1],[0,1,-2]]
#M=[[0,6],[13,6]]
M=[[0,3,1],[3,-4,1],[1,1,-2]]
evals, evecs = la.eig(M)
print("Öz değerler",evals, "   ", len(evals)," adet")
print ("Öz vektör ", evecs)