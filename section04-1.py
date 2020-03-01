# section04-1
# 데이터 타입

import math
v_str1 = "Goodsoul"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = dict(
    name='kim',
    age=25
)
v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

print(type(v_dict))
print(type(v_set))
print(type(v_str1))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print()

i1 = 39
i2 = 939
big_int1 = 20394203948023984029384
big_int2 = 78787878787878787777777
f1 = 1.234
f2 = 3.184
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))
print()

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print((complex(False)))
print()

# 단항 연산자
y = 100
y += 100
print(y)
print()

# 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8)
print(n, m)

print(math.ceil(5.1))
print(math.floor(3.874))
