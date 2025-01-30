"""Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа."""


def length_of_longest_substring(s, changed_syms):
    dct = {}
    max_string_len = 0
    maxim = 0
    j = 0
    for i in range(len(s)):
        dct[s[i]] = dct.get(s[i], 0) + 1
        max_string_len = max(dct[s[i]], max_string_len)
        if i - j + 1 - max_string_len > changed_syms:
            dct[s[j]] = dct.get(s[j], 0) - 1
            j += 1
        maxim = max(i - j + 1, maxim)

    return maxim


if __name__ == '__main__':
    changed_syms = int(input())
    s = input()
    print(length_of_longest_substring(s, changed_syms))
