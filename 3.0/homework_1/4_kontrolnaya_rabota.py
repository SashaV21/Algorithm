"""Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу. Завтра у них контрольная по
математике, и учитель подготовил целых K вариантов заданий. В классе стоит один ряд парт, за каждой из них
(кроме, возможно, последней) на контрольной будут сидеть ровно два ученика. Ученики знают, что варианты будут
раздаваться строго по порядку: правый относительно учителя ученик первой парты получит вариант 1, левый — вариант 2,
правый ученик второй парты получит вариант 3 (если число вариантов больше двух) и т.д. Так как K может быть меньше чем
число учеников N, то после варианта K снова выдаётся вариант 1. На последней парте в случае нечётного числа учеников
используется только место 1.

Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить такой же вариант,
что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно оказаться как можно меньше парт, а при
наличии двух таких мест с равным расстоянием от Пети Вася сядет позади Пети, а не перед ним. Напишите программу,
которая подскажет Васе, какой ряд и какое место (справа или слева от учителя) ему следует выбрать. Если же один и тот же
вариант Вася с Петей писать не смогут, то выдайте одно число -1."""


def count_good_place(num_of_students, num_of_var, rad, pos):
    num_pref_pet = rad * 2 if pos == 2 else rad * 2 - 1
    rad_vas_pref = 0
    pos_vas_pref = 0
    flag1 = 0
    flag2 = 0
    if num_pref_pet - num_of_var > 0:
        pos_vas_pref = (num_pref_pet - num_of_var) % 2
        rad_vas_pref = (num_pref_pet - num_of_var) // 2 if pos_vas_pref == 0 else (num_pref_pet - num_of_var) // 2 + 1
        pos_vas_pref = 1 if pos_vas_pref == 1 else 2
        flag1 = 1
    rad_vas = 0
    pos_vas = 0
    if num_pref_pet + num_of_var <= num_of_students:
        pos_vas = (num_pref_pet + num_of_var) % 2
        rad_vas = (num_pref_pet + num_of_var) // 2 if pos_vas == 0 else (num_pref_pet + num_of_var) // 2 + 1
        pos_vas = 1 if pos_vas == 1 else 2
        flag2 = 1
    if flag1 == 0 and flag2 == 0:
        print(-1)
    elif (rad_vas - rad) == (rad - rad_vas_pref):
        print(rad_vas, pos_vas)
    elif rad_vas == 0:
        print(rad_vas_pref, pos_vas_pref)
    else:
        print(rad_vas, pos_vas)


def main():
    num_of_students = int(input())
    num_of_var = int(input())
    rad = int(input())
    pos = int(input())
    count_good_place(num_of_students, num_of_var, rad, pos)


if __name__ == '__main__':
    main()


