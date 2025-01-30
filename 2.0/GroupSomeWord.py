def GroupWords(words):
    groups = {}
    for word in words:
        sortedword = ''.join(sorted(word))
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans



def groupwords2(words):
    def keybywords(word):
        symcnt = {}
        for sym in word:
            if sym not in symcnt:
                symcnt[sym] = 0
            symcnt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            lst.append(sym)
            lst.append(str(symcnt[sym]))
        return ''.join(lst)

    groups = {}
    for word in words:
        groupkey = keybywords(word)
        if groupkey not in groups:
            groups[groupkey] = []
        groups[groupkey].append(word)
    ans = []
    for groupkey in groups:
        ans.append(groups[groupkey])
    return ans
