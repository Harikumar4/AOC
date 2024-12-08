## star 1

import re
f = open("day3.txt")
data = f.read() 
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(pattern, data)
sum=0
for i in matches:
    sum+=int(i[0])*int(i[1])
print(sum)

## star 2
import re

f = open("day3.txt")
data = f.read()
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
do_pattern = r'do\(\)'
dont_pattern = r'don\'t\(\)'
total = 0
enabled = True 
mul_matches = [(m.group(1), m.group(2), m.start()) for m in re.finditer(pattern, data)]
do_matches = [m.start() for m in re.finditer(do_pattern, data)]
dont_matches = [m.start() for m in re.finditer(dont_pattern, data)]
controls = [(pos, True) for pos in do_matches] + [(pos, False) for pos in dont_matches]
controls.sort() 

for num1, num2, mul_pos in mul_matches:
    current_state = True
    for control_pos, state in controls:
        if control_pos < mul_pos:
            current_state = state
        else:
            break
    if current_state:
        total += int(num1) * int(num2)

print(total)