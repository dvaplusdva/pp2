import re

camel = "ILiveInAlmaty"

snake = re.sub(r'(?<!^)(?=[A-Z])', '_', camel).lower()

print(snake)
