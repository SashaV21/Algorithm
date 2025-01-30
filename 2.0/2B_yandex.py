"""
Петя нашел на чердаке старый телеграфный аппарат и приделал к нему хитроумное устройство, которое может печатать на телеграфной ленте определенное слово (обозначим его X). Петино устройство может напечатать на ленте это слово сколько угодно раз. Петя может заставить аппарат напечатать на ленте и любое другое сообщение, но для этого ему нужно разобрать свое хитроумное устройство, и после этого он уже не сможет печатать сообщение X. А самое главное, что напечатать даже один символ другого сообщения потребует от Пети больше усилий, чем напечатать на ленте слово X с помощью хитроумного устройства.

Петя хочет сделать так, чтобы всем казалось, что ему по телеграфу пришло сообщение Z. Для этого он может (строго в этой последовательности):

- сколько угодно раз напечатать сообщение X

- разобрать хитроумное устройство и посимвольно напечатать еще что-нибудь (назовем это Y)

- оторвать и выбросить начало ленты так, чтобы на оставшейся ленте было напечатано в точности сообщение Z

Поскольку набирать отдельные символы сообщения Y довольно сложно, Петя хочет, чтобы в сообщении Y было как можно меньше символов.

Для лучшего понимания задачи смотрите примеры и пояснения к ним.
"""

x = str(input())
z = str(input())
data = []
if len(x) <= len(z):
    for i in range(len(z)):
        if z[i:].startswith(x):
            data.append(i)
    if len(data) == 0:
        print(z)
    
print(data)




