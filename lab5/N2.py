import re

txt = "sample txt abb ab abbb"

x = re.findall("ab{2,3}", txt)
print(x)
