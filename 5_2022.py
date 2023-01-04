def p1(lines):
    # init stacks per col
    stacks = [[] for _ in range(len(lines[0]) // 4)]

    # populate stacks
    i = 0
    while lines[i+1] != '\n':
        lines[i] = lines[i].replace('\n', ' ')

        for j in range(0, len(lines[i]), 4):
            if lines[i][j+1] != ' ':
                stacks[j // 4].insert(0, lines[i][j+1])

        i += 1

    # skips to instructions
    i += 2

    # perform instructions
    while i < len(lines):
        line = lines[i].split()

        amount = int(line[1])

        # question is 1 indexed, code is 0
        frm = int(line[3])-1
        to = int(line[5])-1

        for _ in range(amount):
            temp = stacks[frm].pop()
            stacks[to].append(temp)

        i += 1

    # print top of each stack
    for s in stacks:
        print(s.pop(), end='')


def p2(lines):
    # init stacks per col
    stacks = [[] for _ in range(len(lines[0]) // 4)]

    # populate stacks
    i = 0
    while lines[i+1] != '\n':
        lines[i] = lines[i].replace('\n', ' ')

        for j in range(0, len(lines[i]), 4):
            if lines[i][j+1] != ' ':
                stacks[j // 4].insert(0, lines[i][j+1])

        i += 1

    # skips to instructions
    i += 2

    # perform instructions
    while i < len(lines):
        line = lines[i].split()

        amount = int(line[1])

        # question is 1 indexed, code is 0
        frm = int(line[3])-1
        to = int(line[5])-1

        # populate temp stack for reverse
        tempstack = []
        for _ in range(amount):
            temp = stacks[frm].pop()
            tempstack.append(temp)

        # reverse back to original order
        for _ in range(amount):
            temp = tempstack.pop()
            stacks[to].append(temp)

        i += 1

    # print top of each stack
    for s in stacks:
        print(s.pop(), end='')


lines = open('input.txt', 'r').readlines()

p1(lines)
print()
p2(lines)
