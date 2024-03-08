import re

sample = "sample. sample,, one two three. m"

x = re.sub(r'[ ,.]', ':', sample)

print(x)
