class Country:
	name = " " 
    conti=""
	gdp = 0
	exp = 0
    imp = 0
    def __init__ (name,conti,gdp,exp,imp):
        self.name = name
        self.conti = conti
        self.gdp = gdp
        self.exp = exp
        self.imp = imp

        #이런식으로 대륙 클래스도 만들 수 있다. 