#-*- coding: UTF-8 -*-#
class Housekim:    
    lastname = u"김"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,where):
        print (u"%s, 여행가네 %s " % (self.fullname,where))
    def __del__(self):
        print("%s dies" % self.fullname)

        