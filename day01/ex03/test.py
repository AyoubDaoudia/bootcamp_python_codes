from matrix import Matrix,Vector

mat=Matrix([[1,2,1],[2,3,1],[3,4,1]])
print("First Matrix \n {}".format(mat))
mat_2=Matrix((3,3))
print("Second matrix by default initialized by zeros\n {}".format(mat_2))
mat_2=Matrix([[1,1,3],[2,3,0],[2,1,4]])
print("Second Matrix filled to perform operations\n {}".format(mat_2))
vec=Vector([1,2,4])
print("Vector created as a subclass of Matrix\n {}".format(vec))
vec_2=Vector(3)
print("Another Vector just to show it can be initialized by size as well, but doesnt work for a Matrix as it needs a shape\n {}".format(vec_2))

r1=mat+mat_2
r2=mat-mat_2
r3=mat*mat_2
r4=mat*vec
r5=4*mat

print("The result for the addition of mat and mat2\n {}".format(r1))

print("The result for the substraction of mat and mat2\n {}".format(r2))

print("The result for the multiplication of mat and mat2\n {}".format(r3))

print("The result for the multiplication of mat and vec which is a vector\n {}".format(r4))

print("The result for the multiplication of mat and a scalar value\n {}".format(r5))