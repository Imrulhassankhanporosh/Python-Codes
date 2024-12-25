summation = 0
i = 1
while i <= 5:
    summation = summation + i
    print("When i is : ", i, "sum is :  ", summation)
    if summation == 3:
        continue
    i = i + 1

    if summation == 12:
        break

print("total sum :", summation)
