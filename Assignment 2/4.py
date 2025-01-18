A={34, 56, 78, 90}
B = {78, 45, 90, 23}
print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))
print("Is A a subset of B",A.issubset(B),"Is B the superset of A",B.issuperset(A))
k=int(input("Enter value to erase"))
for x in A:
    if x==k:
        A.remove(x)