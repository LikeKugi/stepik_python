setA = {2, 4, 7, 3, 6}
setB = {7, 1, 3, 6, 5}

setC = setA & setB

print(*sorted(setC),sep='')

setA = {4, 7, 5, 6, 3, 1}
setB = {7, 1, 3, 6, 5}

setC = setA | setB

print(*sorted(setC),sep='')

setA = {2, 8, 9, 3, 1}
setB = {7, 1, 3, 6, 5}

setC = setA - setB

print(*sorted(setC),sep='')

setA = {2, 8, 7, 3, 1}
setB = {7, 1, 3, 6, 5}

setC = setA ^ setB

print(*sorted(setC),sep='')