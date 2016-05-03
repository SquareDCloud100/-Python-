f = open('./data/oecd.txt')
lines = f.readlines()
gdp=0
conti_cnt = {}
conti_gdp = {}
for line in lines:
    fields=line.split("\t")
#    print fields[0]
    gdp+= float(fields[2])
    con_con ={}
    con_con[fields[1]] = [fields[0], fields[2]]
    if conti_cnt.has_key(fields[0]):
        conti_cnt[fields[0]] += 1
    else:
        conti_cnt[fields[0]] = 1
    if conti_gdp.has_key(fields[0]):
        conti_gdp[fields[0]] += float(fields[2])
    else:
        conti_gdp[fields[0]] = float(fields[2])
for key in conti_cnt.keys():
    print conti_gdp[key]/conti_cnt[key]

for key in con_con.keys():
    if con_con[key][1] > conti_gdp[con_con[key][0]]/conti_cnt[con_con[key][0]]:
        print key
#print conti_cnt
#print conti_gdp
#print gdp/ len(lines)
#{country: [contient, gdp]