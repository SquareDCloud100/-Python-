# -*- coding: utf-8 -*-
import codecs
f = open('./data/oecd.txt', 'r')
out_f = open('./data/result.txt', 'w')
lines = f.readlines()
gdp=0
conti_cnt = {}
conti_gdp = {}
country_gdp = {}

def save_dict(conti, gdp, gdp_dict):
    if gdp_dict.has_key(conti):
        gdp_dict[conti] += gdp
    else:
        gdp_dict[conti] = gdp

for line in lines:
    fields=line.split('\t')

    # country_info[fields[1]] = [fields[0], float(fields[2])]
    gdp += float(fields[2])
    save_dict(fields[0], 1, conti_cnt)
    save_dict(fields[0], float(fields[2]), conti_gdp)
    country_gdp[fields[1]] = [fields[0], float(fields[2])]
"""  
    if conti_cnt.has_key(fields[0]):
        conti_cnt[fields[0]] += 1
    else:
        conti_cnt[fields[0]] = 1
""" 
"""        
    if conti_gdp.has_key(fields[0]):
        conti_gdp[fields[0]] += float(fields[2])
    else:
        conti_gdp[fields[0]] = float(fields[2])
"""
gdp_avg = {}
for key in conti_gdp.keys():
    gdp_avg[key] = conti_gdp[key] / conti_cnt[key]

for key in country_gdp.keys():
    conti=country_gdp[key][0]
    gdp=country_gdp[key][1]
    #print key, conti, gdp_avg[conti], gdp
    if gdp_avg[conti] < gdp:
       # print conti, gdp_avg[conti], key, gdp
        data = "%s, %f, %s, %f\n" % (conti, gdp_avg[conti], key, gdp)
        print data
        #data = conti + str(gdp_avg[conti]) + key + str(gdp)
        out_f.write(data)
out_f.close()
#print gdp_avg
#print conti_cnt
#print conti_gdp
#print gdp / len(lines)
