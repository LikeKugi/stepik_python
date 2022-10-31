class Counter:
    def __init__(self, start=0):
        self.count = start

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0


x = Counter()

print(x.count)
x.count += 1
print(x.count)

y = Counter(5)
print(y.count)

y.inc()
print(y.count)
Counter.inc(y)
print(y.count)
y.reset()
print(y.count)
