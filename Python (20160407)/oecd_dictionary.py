# 딕셔너리를 이용하면 더 잘 만들수 있지 않을까?
# conti_cnt = {"ASIA" : ++ }
# has_key function을 이용하면 conti_cnt.has_key -> key 가 존재하냐를 검사해준다 -> True False 출력 
# if true 면 기존 value +1 else value = 1
f=open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
conti_gdp={}
country_gdp={}
for line in lines:
    splited = line.split('\t')
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


print conti_cnt
print conti_gdp
print gdp_avg

#{'Japan':[ASIA, gdp] 이런식으로 하면 어떨까?}
#a[field[1]] = [f[1
