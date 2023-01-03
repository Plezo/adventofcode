def char_to_prio(s):
    st = set()
    for ch in s:
        if ord(ch) > 96 and ord(ch) < 123:  # lowercase
            st.add(ord(ch)-96)
        elif ord(ch) > 64 and ord(ch) < 91:# uppercase
            st.add(ord(ch)-38)
    return st

def p1(lines):

    res = 0
    for line in lines:
        
        s1 = char_to_prio(line[:len(line)//2])
        s2 = char_to_prio(line[len(line)//2:])

        res += sum(s1.intersection(s2))

    print(res)


def p2(lines):
    
    res = 0
    for i in range(0, len(lines), 3):
        s1 = char_to_prio(lines[i])
        s2 = char_to_prio(lines[i+1])
        s3 = char_to_prio(lines[i+2])

        res += sum(s1.intersection(s2.intersection(s3)))

    print(res)

lines = open('input.txt').readlines()

p1(lines)
p2(lines)
