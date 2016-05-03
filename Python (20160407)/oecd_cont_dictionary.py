#{'Japan':[ASIA, gdp] �̷������� �ϸ� ���?}
#a[field[1]] = [f[1

f=open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
conti_gdp={}
country_gdp={}              # {���� : [���,gdp��]}
for line in lines:
    splited = line.split('\t')
    country_gdp[splited[1]]=[splited[0],splited[2]] # ���� data ����
    if conti_cnt.has_key(splited[0]):               # count �κ�
        conti_cnt[splited[0]] += 1
    else:
        conti_cnt[splited[0]] = 1
    if conti_gdp.has_key(splited[0]):               # gdp �κ�
        conti_gdp[splited[0]] += float(splited[2])
    else:
        conti_gdp[splited[0]] = float(splited[2])   # �� ������ �ʱ�ȭ�ؾ���
gdp_avg={}
for key in conti_gdp.keys():
    gdp_avg[key] = conti_gdp[key] / conti_cnt[key]
for key in country_gdp.keys():                      # ������ ���� Ű
    print key, gdp_avg[country_gdp[key][0]], country_gdp[key][1]
    if gdp_avg[country_gdp[key][0]] < country_gdp[key][1]:
        print [country_gdp[key][0]], key


