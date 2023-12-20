#%%
import re
partial_sum = 0
with open("input.txt") as input:
    for line in input:
        digits = re.findall("\d", line)
        partial_sum += int(str(digits[0]) + str(digits[-1]))

print(partial_sum)