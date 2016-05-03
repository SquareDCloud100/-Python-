f = open('./data/oecd.txt','r')
lines = f.readlines()

gdp = 0;
conti_cnt={}
for line in lines:
   fields= line.split('\t') #쪼개고
   gdp += float(fields[2])  #형변환
  
print gdp / len(lines)
#길이로 나눈다
# 기본 변수는 string이므로 float으로 형변환 필요
# \t 기준으로 쪼개고 3번째 애들끼리 합해서 나누면 되지 않을까
# 딕셔너리를 이용하면 더 잘 만들수 있지 않을까?
# conti_cnt = {"ASIA" : ++ }
# has_key function을 이용하면 conti_cnt.has_key -> key 가 존재하냐를 검사해준다 -> True False 출력 