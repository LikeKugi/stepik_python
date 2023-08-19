from collections import deque

size, n = map(int, input().split())

processing = deque([], size)
timer = 0
time_first = 0

for _ in range(n):
    arrival, duration = map(int, input().split())
    if len(processing) == 0:
        processing.append((arrival, duration))
        timer = arrival if arrival > timer else timer
        print(timer)
        timer += duration
        time_first = timer

    elif arrival >= timer:
        processing.popleft()
        processing.append((arrival, duration))
        timer = arrival
        print(timer)
        timer += duration

    elif len(processing) < size:
        processing.append((arrival, duration))

    else:
        print(-1)
        continue

    print(timer)