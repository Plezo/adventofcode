def p1(lines):
    res = []

    rolling_sum = 0
    for line in lines:
        if line != '\n':
            num = int(line[0:-1])
            rolling_sum += num
        else:
            res.append(rolling_sum)
            rolling_sum = 0

    res.sort()
    print(res[-1])

def p2(lines):
    res = []

    rolling_sum = 0
    for line in lines:
        if line != '\n':
            num = int(line[0:-1])
            rolling_sum += num
        else:
            res.append(rolling_sum)
            rolling_sum = 0

    res.sort()
    print(sum(res[-3:]))


inp = open('input.txt', 'r')
lines = inp.readlines()
p1(lines)
p2(lines)

