import csv

# 데이터 세팅
data_list = []

with open("./resource/test1.csv", "r") as f:
    rd = csv.DictReader(f)
    for i in rd:
        data_list.append(i)

# 초기 출력 메시지
init_msg = """
Welcome!

input command!
a : all print
1 ~ {} : selected data print
i : data insert
q : quit
""".format(
    len(data_list)
)

# 출력 func
def data_print(n):
    # all print
    if n == "a":
        print("\n=================")
        for i in data_list:
            for k, v in i.items():
                print("{:5} : {}".format(k, v))
            print("=================")
    # selected data print
    elif int(n) in range(1, len(data_list) + 1):
        print("\n=================")
        for k, v in data_list[int(n) - 1].items():
            print("{:5} : {}".format(k, v))
        print("=================")


# 데이터 삽입 func
def data_insert():
    with open("./resource/test1.csv", "a") as f:
        wt = csv.writer(f)
        data = []
        for i in data_list[0].keys():
            while True:
                input_data = input("{} : ".format(i))
                if input_data.isalnum() or "-" in list(input_data):
                    data.append(input_data)
                    break
                else:
                    continue
        wt.writerow(data)


# 메인
while True:
    # 명령어 입력
    input_command = input(init_msg)
    if input_command == "q":
        break
    elif input_command == "i":
        data_insert()
        break
    elif not input_command.isalnum():
        print("re input!\n")
        continue
    elif input_command == "a" or int(input_command) in range(1, len(data_list) + 1):
        data_print(input_command)
        break

