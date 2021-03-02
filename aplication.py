a=8 / 2
print(a)
print(type(a))

print((8-4) * 5 + (5%2))

r=5
pi=3.14159
print(2*pi*r)
print(round(2*pi*r))
print(round(2*pi*r, 3))

print(pi*r*r)
print(pi*r**2)
print(pi*(pow(r,2)))

import math

r=5
print(2*math.pi*r)

x=21
if(x%2==0):
    print('X bir cift sayidir')
else:
    print('X bir tek sayidir')


##|4 - 7 | * (4 + 7) =?
print(abs(4-7)*(4+7))

## name=Python
## My name is Python with 3 method  concatination, format, fstring

name= 'Python'
print('My name is '+name)
print('My name is {}'.format(name))
print(f'My name is {name}')


name= 'Python'
age=25
married=True

print(name,age,married) ## arada virgul olmasi bosluk olmasi yeterlidir.


x='100'
y= 50
print(int(x)-y) ## string olan X in int cevrilerek islem yapilmasi icin kullanilir

## kullanicidan ismini alarak buyuk ve kucuk harflerle yazdir

my_string=input('Isminiz nedir')
print(my_string.upper())
print(my_string.lower())




