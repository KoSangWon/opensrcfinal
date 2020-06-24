def calculate(num):
    pi = 0
    a = -1
    denominator = 1
    i = 1
    while i < num:
        a *= -1
        pi += a * 1.0 / denominator
        denominator += 2
        i = i + 1

    return 4*pi

print("i       m(i)")
for i in range(1, 1000, 100):
    print("{0:d}    {1:.4f}".format(i, calculate(i)))
