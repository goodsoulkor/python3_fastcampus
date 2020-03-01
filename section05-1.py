# section05-1
# 조건문

print(type(True))
print(type(False))

# ex1
if True:
    print("Yes")

# ex2
if False:
    print("No")

# ex3
if False:
    print("No")
else:
    print("Yes2")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print()

# 참, 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = ""
if city:
    print("True")
else:
    print("False")
print()

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)

# 산술, 관계 논리 연산자
# 산술 > 관계 > 논리 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10)
print()

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Ok')
else:
    print('sorry')
print()

# 다중 조건문
num = 90

if num >= 90:
    print("num Grade A", num)
elif num >= 80:
    print("num Grade B", num)
elif num >= 70:
    print("num Grade C", num)
else:
    print("sorry")

# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A Ok")
    elif height >= 160:
        print("B Ok")
    else:
        print("Sorry")
else:
    print("Sorry")
