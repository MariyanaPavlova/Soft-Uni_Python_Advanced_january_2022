nums = (float(x) for x in input().split())

dic = {}

for i in nums:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1


for data in dic.items():
    print(f'{data[0]} - {data[1]} times')
