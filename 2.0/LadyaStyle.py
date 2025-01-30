def rookpair(rookcoord):

    def addrook(rook, line):
        if line not in rook:
            rook[line] = 0
        rook[line] += 1

    def findpair(rook):
        pair = 0
        for line in rook:
            pair = rook[line] - 1
        return pair



    linecol = {}
    linerow = {}
    for col, row in rookcoord:
        addrook(linerow, row)
        addrock(linerow, col)
    return findpair(linecol) + findpair(linerow)