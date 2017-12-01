import sys
class T:
    pass
t=T()
print sys.getrefcount(t)
tt=t
print sys.getrefcount(t)
del tt
print sys.getrefcount(t)