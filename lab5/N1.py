import re

txt = "sample txt"

x = re.findall("ab*", txt)
print(x)