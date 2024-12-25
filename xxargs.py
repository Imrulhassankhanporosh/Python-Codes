def add(*numbers):
    summation = 0
    for number in numbers:
        summation = summation + number

    return summation


print(add(10, 20, 10, 5, 5))
