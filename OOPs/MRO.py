class X:
    pass
class Y:
    pass
class Z:
    pass
class P(X,Y):
    pass
class Q(Y,Z):
    pass
class R(Q,P,Z):
    pass

print(R.mro())
