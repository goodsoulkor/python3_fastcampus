# section06
# 함수식 및 람다

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# ex1


def hello(world):
    print("hello", world)


hello("Python")

# ex2


def hello_return(world):
    val = "hello " + str(world)
    return val


str = hello_return("Python!!!!!")
print(str)
print()

# ex3 : 다중 리턴


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# ex4 : 데이터 타입 반환


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul(200)
print(lt)

print()

# ex5
# *args, **kwargs


def args_func(*args):
    # print(args)
    for i, v in enumerate(args):
        print(i, v)


args_func("kim")
args_func("kim", "Park")
args_func("kim", "Park", "Lee")
print()

# kwargs


def kwargs_func(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="kim", name2="Park", name3="Lee")
print()


# 전체 혼합


def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, "Park", "Kim")
example_mul(10, 20, "Park", "Kim", age1=24, age2=35)
print()

# ex6
# 중첩함수(클로져)


def nested_func(num):
    def func_in_func(num):
        print(">>>", num)

    print("in func")
    func_in_func(num + 1000)


nested_func(10000)


# ex7 : hint
def func_mul3(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul3(5.0))
print()

# ex8 : 람다식
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행한다.(heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당


def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))
print()

lambda_mul_10 = lambda x: x * 10

lambda_mul_10(10)


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000))
