# ��ųʸ��� �̿��ϸ� �� �� ����� ���� ������?
# conti_cnt = {"ASIA" : ++ }
# has_key function�� �̿��ϸ� conti_cnt.has_key -> key �� �����ϳĸ� �˻����ش� -> True False ��� 
# if true �� ���� value +1 else value = 1
f=open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
conti_gdp={}
country_gdp={}
for line in lines:
    splited = line.split('\t')
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


print conti_cnt
print conti_gdp
print gdp_avg

#{'Japan':[ASIA, gdp] �̷������� �ϸ� ���?}
#a[field[1]] = [f[1
