# section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대경로

# 파일 읽기
# ex1
f = open("./resource/review.txt", "r")
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()
print()

# ex2
with open("./resource/review.txt", "r") as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print()
print()

# ex3
with open("./resource/review.txt", "r") as f:
    for c in f:
        print(c.strip())

print()
print()

# ex4
with open("./resource/review.txt", "r") as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용 없음
    print(">", content)

print()
print()


# ex5
with open("./resource/review.txt", "r") as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end="####")
        line = f.readline()

print()
print()


# ex6
with open("./resource/review.txt", "r") as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end="*****")

print()
print()

# ex7
score = []
with open("./resource/score.txt", "r") as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : {:6.3}".format(sum(score) / len(score)))

print()
print()

# 파일쓰기
# ex1
with open("./resource/text1.txt", "w") as f:
    f.write("Goodsoul!\n")

# ex2
with open("./resource/text1.txt", "a") as f:
    f.write("Niceguy!\n")

# ex3
from random import randint

with open("./resource/text2.txt", "w") as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write("\n")

# ex4
# writelines : 리스트 -> 파일로 저장
with open("./resource/text3.txt", "w") as f:
    list = ["Kim\n", "Park\n", "Cho\n"]
    f.writelines(list)

# ex5
with open("./resource/text4.txt", "w") as f:
    print("Test Contents1!", file=f)
    print("Test Contents2!", file=f)
