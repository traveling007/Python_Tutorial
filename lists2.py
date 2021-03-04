cities = ['tokyo', 'madrid', 'londra', 'kiev']
print(cities.index('madrid'))

##print(cities.index('ankara'))

##print('ankara' in cities)
##print('tokyo' in cities)

for city in cities: 
#   print(city)
    print(f'Gezilen sehir : {city}')
    print('Gezilecek sehir kalmadi') ## ikisi ayni dongude oldugu icin her bir deger icin yazacaktir.
print('Gezilecek sehir kalmadi')


str_cities = 'tokyo,madrid,kiev'
## print(str_cities)
my_list = str_cities.split(', ')
print(my_list)


str_email = 'pythonyazilim@gmail.com'
print(str_email)
my_list2=str_email.split('@')
print(my_list2)


for number in range(1,11):
    print(number)

for number in range(2,21,2):
    print(number)

numbers=list(range(1,11))
print(numbers)

numbers2=[number for number in range(1,11)]
print(numbers2)


cities=['izmir','ankara','istanbul']
##print(cities)
##cities2=cities
##print(cities2)
##cities.append('artvin')
##print(cities)
##print(cities2)

print(cities)
cities2=cities[:]
print(cities2)
cities.append('artvin')
print(cities)
print(cities2)



