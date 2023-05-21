
a = 5
b = a
a = 6
print(a, b)


c = [1, 2, 3]
d = c
c.pop()
print(c, d)


def foo(x):
    x += 1

a = 1
foo(a)
print(a)


def bar(x):
    x.append(100)

c = [1,2,3]
bar(c)
print(c)
