#-*- coding: UTF-8 -*-#
class Housepark:    
    self.lastname = "박"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self,where):
        print ("%s, 여행가네 %s " % (self.fullname,where))
    def __del__(self):
        print("%s dies" % self.fullname)

