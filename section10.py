# section10
# 파이썬 예외처리

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요

# syntaxError : 잘못된 문법
# print('Test)
# if True
#     pass

# NameError : 참조 변수 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3])

# KeyError
dic = {"name": "Kim", "age": 33, "city": "Seoul"}
# print(dic["hobby"])
print(dic.get("hobby"))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 시에 예외
import time

print(time.time())
# print(time.month())

# ValueError : 참조 값이 없을 때
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError
# f = open("test.txt", "r")

# TypeError
x = [1, 2]
y = (1, 2)
z = "test"

# print(x + y)
# print(x + z)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# ex1
name = ["Kim", "Lee", "Park"]

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError:
    print("Not Found it! - Occurred ValueError!")
else:
    print("Ok! else!")

# ex2
try:
    z = "Jin"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except:
    print("Not Found it! - Occurred Error!")
else:
    print("Ok! else!")


# ex3
# finally
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError:
    print("Not Found it! - Occurred ValueError!")
else:
    print("Ok! else!")
finally:
    print("Finally ok!")

# ex4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print("try")
finally:
    print("Ok Finally")

# ex5
try:
    z = "cho"
    x = name.index(z)
    print("{} Found it! in name".format(z, x + 1))
except ValueError as v:
    print(v)
except IndexError:
    print("Not Found it! - Occurred IndexError!")
except Exception:  # 순서가 맨 마지막이어야 한다.(모든 에러를 잡기 때문에)
    print("Not Found it! - Occurred ValueError!")
else:
    print("Ok! else!")
finally:
    print("Finally ok!")

# ex6
# 강제로 예외 발생 : raise
try:
    a = "333"
    if a == "Kim":
        print("Ok")
    else:
        raise ValueError
except ValueError:
    print("Warning!")
except Exception as e:
    print(e)
else:
    print("Ok")

