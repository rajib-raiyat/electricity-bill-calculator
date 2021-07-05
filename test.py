def calc_bill():
    units = int(input("Number of unit consumed: "))
    total_amount = 0

    if 0 < units <= 50:
        total_amount += units * 3.05
    elif 0 < units <= 75:
        total_amount += (50 * 3.05) + (units - 50) * 4.00
    elif 76 < units <= 200:
        total_amount += (50 * 3.05) + ((75 - 50) * 4) + (units - 75) * 5.45
    elif 201 < units <= 300:
        total_amount += (50 * 3.05) + ((75 - 50) * 4) + ((200 - 75) * 5.45) + (units - 200) * 5.70
    elif 301 < units <= 400:
        total_amount += (50 * 3.05) + ((75 - 50) * 4) + ((200 - 75) * 5.45) + (units - 200) * 5.70
    else:
        print(0)

    print(total_amount)


calc_bill()  # call the function with argument

# if v[0][0] < units <= v[0][1]:
#     total_amount += units * v[0][2]
# elif v[1][0] < units <= v[1][1]:
#     total_amount += (units * v[0][2]) + ((units - v[0][1]) * v[1][2])
# elif v[2][0] < units <= v[2][1]:
#     total_amount += (units * v[0][2]) + ((v[1][1] - v[0][1]) * v[1][2]) + (units - v[1][1]) * v[2][2]
# elif v[3][0] < units <= v[3][1]:
#     total_amount += (units * v[0][2]) + ((v[1][1] - v[0][1]) * v[1][2]) + ((200 - 75) * 5.45) + (units - 200) * 5.70
# elif v[4][0] < units <= v[4][1]:
#     total_amount += (units * v[0][2]) + ((v[1][1] - v[0][1]) * v[1][2]) + ((200 - 75) * 5.45) + (units - 200) * 5.70
# else:
#     total_amount += (units * v[0][2]) + ((v[1][1] - v[0][1]) * v[1][2]) + ((200 - 75) * 5.45) + (units - 200) * 5.70
