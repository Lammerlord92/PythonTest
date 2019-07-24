import datetime

dt=datetime.datetime.now()
print(dt)
print(dt.year)

print(dt.tzinfo)

print(datetime.datetime(2000,1,1,0,0))


print(dt.isoformat())
print(dt.strftime("%Y%B%d"))
print(dt.strftime("%Y%m%d"))
import locale
print(locale.setlocale(locale.LC_ALL,'es-ES'))
print(dt.strftime("%A, %d %B %Y"))
print(locale.setlocale(locale.LC_ALL,'zh-CN'))
print(dt.strftime("%A, %d %B %Y"))
print(locale.setlocale(locale.LC_ALL,'ja-JA'))
print(dt.strftime("%A, %d %B %Y"))
print(locale.setlocale(locale.LC_ALL,'gd'))
print(dt.strftime("%A, %d %B %Y"))
print(locale.setlocale(locale.LC_ALL,'ru'))
print(dt.strftime("%A, %d %B %Y"))
print(locale.setlocale(locale.LC_ALL,'es-ES'))
print(dt.strftime("%A %d de %B del %Y"))

t=datetime.timedelta(days=14,hours=4,seconds=1000)
en_dos_semanas=dt+t

print(en_dos_semanas)
