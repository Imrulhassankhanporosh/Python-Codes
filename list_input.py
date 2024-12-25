a = (input("Enter the numbers: "))

l = a.split()

# inputted string elements are taken into a list

summation = 0

for count in l:
    summation = summation + int(count)
    # string type cast to int
    print(summation)
