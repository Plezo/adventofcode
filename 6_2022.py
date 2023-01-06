def p1(line):
    for i in range(4, len(line), 1):
        marker = line[i-4:i]
        if len(set(marker)) == len(marker):
            print(i)
            break


def p2(line):
    for i in range(14, len(line), 1):
        marker = line[i-14:i]
        if len(set(marker)) == len(marker):
            print(i)
            break

lines = open('input.txt', 'r').readlines()

p1(lines[0])
p2(lines[0])
