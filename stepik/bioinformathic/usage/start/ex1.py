a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)

def h():
    print("- H")
    print("- 12")
    print("H - end")

def f():
    print("- F")
    g(h)
    print("F - end")

def g(a):
    print("- G - ",a)
    a()
    print("G - end")

print("\nMODULE")
g(f)