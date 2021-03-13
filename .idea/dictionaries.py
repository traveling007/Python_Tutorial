"""monster_1 = {'name': 'guru','power':10, 'color': 'red'}

print(monster_1)
monster_1['position']=100
print(monster_1)
print(monster_1['position'])
print(monster_1.get('boy')) ##burada get ile hata vermemesi icin kullaniriz. girilen key yok ise None olarak donus olur
monster_1['position']=100
print(monster_1)
monster_1.update({'name':'GURU', 'power':20})
print(monster_1)
monster_1.pop('power') ##del ile silersek tekrar getiremeyiz
print(monster_1)

"""
"""
poplan = monster_1.pop('power')
print(monster_1)
print(poplan)
"""
"""
monster_1.clear()
print(monster_1)
"""
"""
print(len(monster_1))
"""
"""
print(monster_1.keys())
print(monster_1.values())
print(monster_1.items())

for key in monster_1:
    print(key)

for key in monster_1.keys():
    print(key)

for value in monster_1.values():
    print(value)
for x in monster_1.values():
    print(x) 
"""
"""
monster_1 = {'name': 'guru','power':10, 'color': 'red'}
print(type(monster_1))
print(monster_1)
print(monster_1['name'])
"""



"""my_friend = {'name': 'deniz','age':40,'gender': 'woman'}"""

my_friends = [
    {'name':'deniz','age':40},
    {'name':'bulent','age':44}
]
print(my_friends[0]['age'])
