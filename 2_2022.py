def p1(lines):
    mp = {
        # (wins against, equal to, value)
        'X': ('C', 'A', 1),
        'Y': ('A', 'B', 2),
        'Z': ('B', 'C', 3)
    }

    score = 0
    for line in lines:
        if mp[line[2]][0] == line[0]:
            score += 6
        elif mp[line[2]][1] == line[0]:
            score += 3

        score += mp[line[2]][2]
        
    print(score)

def p2(lines):
    mp = {
        # (wins against, loses to, value)
        'A': ('C', 'B', 1),
        'B': ('A', 'C', 2),
        'C': ('B', 'A', 3)
    }

    score = 0
    for line in lines:
        if line[2] == 'X':      # lose
            score += mp[mp[line[0]][0]][2]
        elif line[2] == 'Y':    # draw
            score += 3 + mp[line[0]][2]
        elif line[2] == 'Z':    # win
            score += 6 + mp[mp[line[0]][1]][2]
    
    print(score)

inp = open('input.txt', 'r')
lines = inp.readlines()

p1(lines)
p2(lines)
