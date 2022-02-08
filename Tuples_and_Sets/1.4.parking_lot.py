n = int(input())
lot = set()

for i in range(n):
    directions, car_num = input().split(", ")
    if directions == "IN":
        lot.add(car_num)
    elif directions == "OUT":
        lot.remove(car_num)

if lot:
    print("\n".join(lot))
else:
    print('Parking Lot is Empty')