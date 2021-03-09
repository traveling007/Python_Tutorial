capitals=('tahran','ankara','maadrid','tiflis') ##tuple methodunda normal parantez kullaniyoruz

"""
print(len(capitals))
print(capitals[0])
print(capitals[1:3])
capitals[0] ='izmir' ## varolan nesneleri degistirilemez oldugu icin hata verecektir. tuple medhodu
"""

"""
for capital in capitals:
    print(capital)
"""

"""
print(capitals)
capitals=('berlin', 'roma')
print(capitals)

"""

"""
del capitals
print(capitals)
"""

"""
cities={'izmir','ankara','istanbul','kars'}
print(type(cities))
print(cities)
"""
"""
cities={'izmir','ankara','istanbul','kars','istanbul'} ## set taniminda iki tane ayni degisken olsa da tek degisken alir
print(type(cities))
print(cities)

"""
"""
cities={'izmir','ankara','istanbul','kars','istanbul'}
##print(cities[0]) ## set yapisinda indeks yoktur. bu yuzden hata verir
print(cities)
cities.add('gaziantep')
print(cities)
cities.update(['edirne','trabzon'])
print(cities)

"""
"""
cities={'izmir','ankara','istanbul','kars','istanbul'}
print(cities)
cities.remove('ankara') ##yanlis veri yazarsak ankarax gibi hata verecektir. ama discard ile hata vermez
print(cities)

"""
"""
cities={'izmir','ankara','istanbul','kars','istanbul'}
print(cities)
cities.discard('izmirx')## burada icerisinde bulunmayan nesneyi dahi yazmis olsak hata vermez. normal yazar 
print(cities)

"""

"""
cities={'izmir','ankara','istanbul','kars','istanbul'}
cities.clear()
print(cities)

"""
cities={'izmir','ankara','istanbul','kars','istanbul'}
del cities
print(cities)






