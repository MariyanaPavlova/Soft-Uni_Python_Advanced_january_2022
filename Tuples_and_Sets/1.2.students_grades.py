n = int(input())
dict = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in dict:
        dict[name] = []
    dict[name].append(grade)


for data in dict.items():
    print(f'{data[0]} -> {" ".join(str(f"{x:.2f}") for x in data[1])} (avg: {sum(data[1])/len(data[1]):.2f})')