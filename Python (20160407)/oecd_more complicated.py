f=open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
conti_gdp={}
country_gdp={}              # {국가 : [대륙,gdp값]}
for line in lines:
    fields = line.split('\t')
    fields.keys
    country_info[fields[1]] = [fields[0], float(fields[2])] # 하지만 - 가 있기 떄문에 오류가 난다!
    for info in country_info.keys():
        if conti_gdp.has_key(info[0]):
            conti_gdp[info[0]] += info[1]
        else:
            conti_gdp[info[0]] = info[1]




"""
-를 어떻게 걸러낼 겟인가?
우리에게는 a.index('-') 가 있다.
while a.index('-'):
저거 잘 이해안되네 ;; 교수님한테 물어봐야겠다.

파일쓰기 f.write(data)라고 할 때 데이터는 항상 string 형태여야한다.
"""  
