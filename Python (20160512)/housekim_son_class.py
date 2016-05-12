from housekim_class import Housekim
class HousePark(Housekim):
        lastname="박"
        def travel(self,where,day):
            print "%s %s 여행 %d 가네." % (self.fullname,where,day)

