# -*- coding: utf-8 -*-
import codecs
from oecd_class import Country
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
    c = Country(fields[0],fields[1],fields[2],fields[5],fields[6])
    countrises.append(c)
    save_dict(fields[0],1,conti_cnt)
    save_dict(fields[0], float(fields[2]), conti_gdp)
    country_gdp[fields[1]] = [fields[0], float(fields[2])]

    # country_info[fields[1]] = [fields[0], float(fields[2])]
    