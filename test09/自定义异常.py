#coding=utf8
class ShortIntExec(Exception):
    #自定义异常
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast
def main():
    try:
        s=input("请输入--》")
        if len(s)<3:
            #raise引发一个你定义的异常
            raise ShortIntExec(len(s),3)
    except ShortIntExec as ret:
        # pass
        print ("ShortIntExec:输入的长度是%d,长度至少应是%d"(ret.length,ret))
    else:
        print ("没有异常发生。")

main()