cities= ['barcelona', 'floransa', 'moskova', 'belgrad', 'tahran']
print(cities)
print(cities[0]) ##indeks numarasi
print(len(cities)) ## indeks sayisi ogrenme
print(cities[-1]) ## en sagdan baslar
print(cities[0:2]) 
print(cities[:2])

cities[0]='tiflis' ## degisiklik yapmak istersek
print(cities)

cities.append('amazon')
print(cities)

cities.append('roma')
print(cities)

cities.insert(2, 'roma')
print(cities)

del cities[0] ## bu method ile silersek tekrar getiremeyiz
print(cities)
cities.pop()
print(cities) ## bu method ile sildigimiz liste elemanina ulasabiliriz
cities2=cities.pop()
print(cities2)
cities.remove('belgrad')
print(cities)

cities.sort() 
print(cities)
cities.sort(reverse=True)
print(cities)

print(sorted(cities))
print(cities)

numbers=[12,28,11,20]
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))


