#coding=utf8
f=open("sendmsg.py","r")
content=f.read()
print content
f.close()
print "-----------"

f=open("sendmsg.py","r")
content=f.readlines()
print content
for temp in content:
  print temp
f.close()
lst=eval(str([1,2,3,4]))
print lst
print type(lst)
# 阮军磊（服务器）
# 耿雷（iOS）
# 郭小花（女）
