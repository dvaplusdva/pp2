import re

sample = "BomboclatOreoMilkShake"

x = re.sub(r'(?<!^)(?=[A-Z])', ' ', sample)

print(x)
