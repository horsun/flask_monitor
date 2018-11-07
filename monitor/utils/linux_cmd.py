import os

print(os.popen("vmstat -s").read())
print(os.popen('iostat').read())
print(os.popen('netstat -anp|grep 8000').read())
print(os.popen('ps -ef|grep python').read())
