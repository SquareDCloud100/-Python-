#{'Japan':[ASIA, gdp] 이런식으로 하면 어떨까?}
#a[field[1]] = [f[1

f=open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
conti_gdp={}
country_gdp={}              # {국가 : [대륙,gdp값]}
for line in lines:
    splited = line.split('\t')
    country_gdp[splited[1]]=[splited[0],splited[2]] # 국가 data 저장
    if conti_cnt.has_key(splited[0]):               # count 부분
        conti_cnt[splited[0]] += 1
    else:
        conti_cnt[splited[0]] = 1
    if conti_gdp.has_key(splited[0]):               # gdp 부분
        conti_gdp[splited[0]] += float(splited[2])
    else:
        conti_gdp[splited[0]] = float(splited[2])   # 그 값으로 초기화해야지
gdp_avg={}
for key in conti_gdp.keys():
    gdp_avg[key] = conti_gdp[key] / conti_cnt[key]
for key in country_gdp.keys():                      # 국가로 도는 키
    print key, gdp_avg[country_gdp[key][0]], country_gdp[key][1]
    if gdp_avg[country_gdp[key][0]] < country_gdp[key][1]:
        print [country_gdp[key][0]], key


