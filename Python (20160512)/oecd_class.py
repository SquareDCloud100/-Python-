from oecd_continent_class import Continent

class Country(Continent):

    def __init__ (name,conti,gdp,exp,imp):
        self.name = name
        self.conti = conti
        self.exp = exp
        self.imp = imp
        self.conti=conti;
        
      # 부모 ㅡ 자식관계