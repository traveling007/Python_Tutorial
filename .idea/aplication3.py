

"""
new_string='asdsdfdgdkiyoerpfgfdgr'
new_set={harf for harf in new_string}
print(new_set)
"""

"""
new_set={'ahmet','mehmet','ayse','fatma'}
new_set.add('Pyhton')
new_list=list(new_set)
print(new_list)
"""


"""
new_tuple=('5','izmir',28,'ankara','5','izmir')

new_set=set(new_tuple)
print(new_set)## set yazilim

new_set=set(new_tuple)
new_tuple2=tuple(new_set)
print(new_tuple2) ## bu yazim tuple yazilimi

##kisayoldan bulmak icin
new_tuple2=tuple(set(new_tuple))
print(new_tuple2)
"""

"""
cities= ('istanbul','ankara','izmir')
print('izmir' in cities)
print('balikesir' in cities) 
"""

"""
new_tuple=(4,8, [1,20])

new_tuple[0]=50
print(new_tuple)## tuple nesnesini assignment degeri yapamayiz


new_tuple[-1][0]=100
print(new_tuple) ##tuple icerisinde list olursa o elemani degistirebiliriz.
"""

"""
new_tuple=('istanbul','balikesir')
print(type(new_tuple))
"""

"""
cities= ('izmir','ankara','istanbul','agri')
print(type(cities))
print(cities[0])
print(cities[-1])
print(cities[:2])
print(cities[-2:])

"""

"""
new_tuple=('izmir',[28,'mahmut'],(2,4,6),100)
print(new_tuple[1][1])
print(new_tuple[2][-1])

"""

"""
new_tuple = ('istanbul','balikesir')
print(type(new_tuple))

new_tuple = ('istanbul',)
print(type(new_tuple)) ## eger virgul koymazsak tek deger olarak algilar ve string olarak alir.
"""