import numpy as np
a=int(input("Enter the number of Rows:"))
b=int(input("Enter the number of Columns:"))
x=[]
for i in range(a):
    x.append([0]*b)
for i in range (a):
    for j in range(b):
        print("Enter Element No:",i,j)
        x[i][j] = int(input())
print(np.matrix(x))
dict={1 :'Determinant',2 :'Rank',3 :'Matrix power',4:'Inverse',5: 'Eigen values',6:'Frobenius norm',7:'Transpose',8:'Trace',9:'program is end'}
print(dict)
d=input("choose the required opearion from dictionary:")
if d==1:
	if a==b:
		print("Determinant of the matrix:",np.linalg.det(x))
	else:
		print("please enter equal number of rows and columns")
elif d==2:
	print("rank of matrix:",np.linalg.matrix_rank(x))
elif d==3:
	p=input("enter power:")
	if a==b:
		print("Power of matrix:",np.linalg.matrix_power(x,p))
	else:
		print("please enter equal number of rows and columns")
elif d==4:
	if a==b:
		print("Inverse of matrix:",np.linalg.inv(x))
	else:
		print("please enter equal number of rows and columns")
elif d==5:
	if a==b:
		print("Eigen values of matrix:",np.linalg.eigvals(x))
	else:
		print("please enter equal number of rows and columns")
elif d==6:
	print("Frobenius norm of matrix:",np.linalg.norm(x))
elif d==7:
	print("Transpose of matrix:",np.transpose(x))
elif d==8:
	if a==b:
		print("Trace of matrix:",np.trace(x))
	else:
		print("please enter equal number of rows and columns")	
