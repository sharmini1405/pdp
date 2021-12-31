width = 0

def partialDigest(L):
    global width
    width = max(L)
    delete(width, L)
    X = [0, width]
    place(L, X)


def place(L, X):
    if len(L) == 0:
        X.sort()
        print(X)
        return

    y = max(L)

    arr1 = D(y, X)
    if testSubset(arr1, L):
        addToX([y], X)
        removeFromL(arr1, L)
        place(L, X)
        removeFromX([y], X)
        addToL(arr1, L)
    arr2 = D(abs(width - y), X)
    if testSubset(arr2, L):
        addToX([abs(width - y)], X)
        removeFromL(arr2, L)
        place(L, X)
        removeFromX([abs(width - y)], X)
        addToL(arr2, L)
    return

def delete(width, L):
    if width in L:
        L.remove(width)

def addToX(val, X):
    for a in val:
        X.append(a)


def removeFromX(val, X):
    for a in val:
        delete(a, X)


def addToL(val, X):
    for a in val:
        X.append(a)


def removeFromL(val, L):
    for a in val:
        delete(a, L)


def D(y, X):
    arr = []

    for v in X:
        arr.append(abs(v - y))

    return arr


def testSubset(D, L):
    for a in D:

        if a not in L:
            return False

    return True


L = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
partialDigest(L)
