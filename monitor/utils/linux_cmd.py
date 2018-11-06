import os

print(os.popen("vmstat -s").read())
print(os.popen('iostat').read())
