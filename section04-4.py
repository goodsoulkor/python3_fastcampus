# section04-4
# 딕셔너리, 집합 자료형

# 딕셔너리(Dict) : 순서 X, 중복 X, 수정 O, 삭제 O
# Key, Value

# 선언
a = {'name': 'Kim', 'Phone': '010-1111-2222', 'birth': 800612}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name'])
print(a.get('name1'))
print(c['arr'][1:2])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))
temp = list(a.keys())
print(temp[1:3])

print(a.values())

print(a.items())
print(1 in b)

# 집합(set)
# 순서 x, 중복 x
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(c)
print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)

s3.remove(15)
print(s3)
print(type(s3))
