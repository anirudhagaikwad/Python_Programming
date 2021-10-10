
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)#Union is performed using | operator.

print(A.union(B))#union using Function

#Intersection of A and B is a set of elements that are common in both sets.
print(A & B) #Intersection is performed using & operator.
# Intersection can be accomplished using the method intersection().
print(A.intersection(B))


print(A - B)#Difference is performed using - operator. 
""""
Difference of A and B (A - B) is a set of elements that are only in A 
but not in B.
B - A is a set of element in B but not in A.
"""
#Same can be accomplished using the method difference().
print(A.difference(B))