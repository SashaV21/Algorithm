"""Как известно, два наиболее распространённых формата записи даты — это европейский
(сначала день, потом месяц, потом год) и американски (сначала месяц, потом день, потом год).
Системный администратор поменял дату на одном из бэкапов и сейчас хочет вернуть дату обратно.
Но он не проверил, в каком формате дата используется в системе. Может ли он обойтись без этой информации?
Иначе говоря, вам даётся запись некоторой корректной даты.
Требуется выяснить, однозначно ли по этой записи определяется дата
даже без дополнительной информации о формате."""

a, b, c = map(int, input().split())
if 12 >= a != b <= 12:
    print(0)
else:
    print(1)
