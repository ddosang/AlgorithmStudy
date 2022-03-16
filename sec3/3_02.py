import math

word = input()
res = 0
count = 0

for c in word:
    if c.isdecimal():
       res = res * 10 + int(c)


end = int(math.sqrt(res))
for i in range(1, end):
    if res % i == 0:
        count += 1

count *= 2
if int(math.sqrt(res)) == math.sqrt(res):
    count += 1

print(res, count)
