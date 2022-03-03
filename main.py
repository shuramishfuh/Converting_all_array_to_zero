import itertools

asum = [
    [[0, 1], [0, 1]],
    [[0, 0], [0, 0]],
    [[1, 1], [0, 0]],
    [[0, 0], [1, 1]],
    [[1, 0], [1, 0]],
    [[1, 1], [1, 1]],
    [[0, 1], [1, 0]],
    [[1, 0], [0, 1]],

]  # success arrays
c = ["0101", "0000", "1100", "0011", "1010", "1111", "0110", "1001", ]  # representation of compressed success arrays


# check if array could be switched off or not
# build smaller arrays of 2X2 each time from start
# to end of array. If compressed string is not in the
# predefined list return false else continue till
# end then return true
# m=row, n = col, a = array
def findOdd(m, n, a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:  # single row
        print("he")
        compressedRow = ""
        for x in a:
            for i in x:
                compressedRow += str(i)
        if str(compressedRow).count('0') > 0 and str(compressedRow).count('0') > 0:
            return -1
        else:
            return 0

    for row in range(m - 1):
        for col in range(n - 1):
            if str(str(a[row][col]) + str(a[row][col + 1]) + str(a[row + 1][col]) + str(a[row + 1][col + 1])) not in c:
                return -1
    return 0


# print if solvable if findOdd returns true or otherwise
def canTurnOff(m, n, a):
    print("solvable" if findOdd(m, n, a) == 0 else "not solvable")


# example
d = [
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1],

]

b = [[0, 1], [0, 1]]
canTurnOff(3, 4, d)
