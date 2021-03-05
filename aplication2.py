dersler=['matematik','fizik','kimya','ingilizce', 'turkce']
print(dersler)
print(dersler[1].upper())
print(dersler[-1].upper())
print(dersler[4].upper())


print(dersler[1:3])
print(dersler[:2])
print(dersler[-2:])

dersler=['matematik',['fizik','kimya'],'ingilizce', 'turkce']
print(dersler[1])
print(dersler[1][0])
print(dersler[1][1].upper())
print(dersler[len(dersler)-1])

print(len(dersler))
dersler.append('tarih')
print(dersler)

dersler[len(dersler):]=['cografya']
print(dersler)

dersler=['matematik','fizik','kimya','ingilizce', 'turkce']

dersler.insert(0,'tarih')
print(dersler)
dersler.insert(len(dersler), 'cografya')
print(dersler)

dersler=['matematik','fizik','kimya','ingilizce', 'turkce']

del dersler[2]
print(dersler)

dersler.remove('turkce')
print(dersler)

numbers=[8, 4, 5, 6, 7, 9, 2, 1, 3, ]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


dersler=['matematik','fizik'],['kimya','ingilizce'], ['turkce', 'tarih']
dersler2=[]
dersler2.append(dersler[0][-1])
dersler2.append(dersler[1][-1])
dersler2.append(dersler[2][-1])
print(dersler2)

## kisa yol olarak

dersler2 = []
for ders in dersler2:
    dersler2.append(ders[-1])

print(dersler2)


## 1 den 10 a kadar olan sayilarin karelerinin alalim

squares=[]
for num in range(1,11):
    squares.append(num**2)

print(squares) 

squares=[num**2 for num in range(1,11)]
print(squares)