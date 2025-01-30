num_of_look = int(input())
data_of_sv = [set() for _ in range(num_of_look)]

for i in range(num_of_look):
    pwd = set(input())
    data_of_sv[i] |= pwd

num_of_number = int(input())
data_of_number = [set() for _ in range(num_of_number)]

data_of_num_list = []
for i in range(num_of_number):
    pwd = input()
    data_of_num_list.append(pwd)
    data_of_number[i] |= set(list(pwd))

data = []

for i in range(num_of_number):
    count = 0
    for j in range(num_of_look):
        if data_of_number[i] >= data_of_sv[j]:
            count += 1
    data.append(count)

max_num_sv = max(data)

for i in range(num_of_number):
    if data[i] == max_num_sv:
        print(data_of_num_list[i])

