def p1(lines):
    
    res = 0
    for line in lines:
        interval1 = [int(i) for i in line.split(',')[0].split('-')]
        interval2 = [int(i) for i in line.split(',')[1].split('-')]

        # interval2 in interval1
        if interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
            res += 1
        # interval1 in interval2
        elif interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
            res += 1
    
    print(res)

def p2(lines):
    res = 0
    for line in lines:
        interval1 = [int(i) for i in line.split(',')[0].split('-')]
        interval2 = [int(i) for i in line.split(',')[1].split('-')]
        
        """
        intersect example:
        1-6, 3-8
        max(1, 3) -> 3
        min(6, 8) -> 6
        3 <= 6 -> true

        no intersect example:
        1-3, 5-8
        max(1, 5) -> 5
        min(3, 8) -> 3
        5 <= 3 -> false
        """
        if max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1]):
            res += 1

    print(res)


lines = open('input.txt', 'r').readlines()

p1(lines)
p2(lines)
