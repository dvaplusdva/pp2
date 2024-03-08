import re

sample = "ILikeToEatAnIceCream"

x = re.split(r'(?=[A-Z])', sample)

print(x)
