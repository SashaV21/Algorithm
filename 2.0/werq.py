# longest common prefix
# сортировка проходит таким образом, что сверяется по буквам каждое слово, то есть по краям сто процентов встанет такие
# слова у которых различается та или иная буква, а в центре будет то, что у них похоже в любом случае.
# гениально ептать

def longestCommonPrefix(strs):
    ans = ""
    strs = sorted(strs)
    print(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans


def main():
    print(longestCommonPrefix(["собака", "солнце", "собд"]))


if __name__ == '__main__':
    main()
