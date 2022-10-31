class D:
    pass


class C:
    pass


class B(D, C):
    pass


class E:
    pass


class A(B, E):
    pass


print(issubclass(A, A))
print(issubclass(C, D))
print(issubclass(A, D))
print(issubclass(C, object))

print()

x = A()
print(isinstance(x,A))

print()

print(A.mro())