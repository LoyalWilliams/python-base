#coding=utf8
try:
    open("xx.txt")
    print "-----"
except NameError:
    print "hehee"
# except FileNotFoundError