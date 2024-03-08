import re

txt = "sample txt ahdfghdfgnb dsjbfsa akghllnj vbcfnvavjnvbb"

x = re.findall("a.*?b", txt)

print(x)