import re

txt = "sample txt b_s_a_v ddd"

x = re.findall("[a-z]+_[a-z]+", txt)

print(x)