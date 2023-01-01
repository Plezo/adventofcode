lines = []

inp = open('input.txt', 'r')
lines = inp.readlines()
inp.close()

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
