import re

txt = "sample txt ABjhblksdFAA j;b jAJSDB Fj AKJBfsdkjdjffbdKJ FBSKD"

x = re.findall("[A-Z]{1}[a-z]+", txt)

print(x)