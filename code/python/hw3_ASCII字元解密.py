#*************************************************************************************************************************
#   Name:   林姿岑
#
#   Class:  資管系三年級
#
#   SID:    S05490061
#
#   Program Name: hw3.py
#
#   Function:   (a) 顯示解密的原文。 
#               (b) 將上述(a)中的原文解密結果再度加密回去；並與原始解密前的字串作資料比對，
#                   如果任何一個字、一個標點符號或任何一個空格都沒有錯誤與遺失的話，
#                   則在螢幕上顯示出 ”加密內容經比對後正確無誤！”等字樣。  
#               (c) 計算並顯示執行(a)解密之後原文中的字元個數，此處包含標點符號與空白。 
#               (d) 將執行(a)解密之後的原文做文字處理，包含(1)字元分類與(2)計算相同字元出現 的次數，並將結果顯示列印出來。 
#               (e) 報告完成時當下的年月日時分秒。 
#
#   Homework: No.3
#
#   Limitations:(1). 無法將字典中結果分離印出
#
#   Date: 2018/11/11
#*************************************************************************************************************************

import datetime     # 匯入datetime模組，完成功能要求(e)

s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

#------(a) 顯示解密的原文。------#

d = {}

#
# 參考用：ASCII字元解密對應表(方法)
#

for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
        #use ROT13 加密
        
print("(a)小題 : 顯示解密的原文內容")
print("".join([d.get(c, c) for c in s]))
print()
#使用join函式連接
#Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。
#d.get(c, c)， 當c不在加密密碼中時，使用本身代替，這樣實現了對標點符號等的支持

#------(b)小題 : 比對加密前後是否相同------#

print("(b)小題 : 比對加密前後是否相同")
q=("".join([d.get(c, c) for c in s]))#把解密結果放入字串q

#
#ASCII反向解密
#
R = {}
for a in (65, 97):
    for j in range(26):
        R[chr((j+13) % 26 + a)] =chr(a+j)

r=("".join([R.get(a, a) for a in q]))#把加密結果放入r

if r == s :#比對是否相同
    
    print( "比對結果: 加密內容經比對後正確無誤！")
    print()

#------(c)小題 : 計算並顯示執行(a)解密之後原文中的字元個數，此處包含標點符號與空白------#
    
count_1 =len(q)#Python 字典(Dictionary) len() 函数可计算字典元素個數
print("(c)小題 : 計算並顯示執行(a)解密之後原文中的字元個數，此處包含標點符號與空白")
print("原文解密後的字元個數",count_1)
print()

#------(d)小題 :將執行(a)解密之後的原文做文字處理，包含----------------#
#---------(1)字元分類-------------------------------------------------#
#---------(2)計算相同字元出現 的次數，並將結果顯示列印出來。-----------#

print("(d)小題 :  將執行(a)解密之後的原文做文字處理，包含(1)字元分類與(2)計算相同字元出現 的次數，並將結果顯示列印出來。 ")
dic={w:q.count(w) for w in set(q)}#使用字典生成式進行處理
print(sorted(dic.items()))#使用sorted排序按照键值，並印出
print()

#---------(e) 報告完成時當下的年月日時分秒。-------------#

print( """\n        
**********************************************************************************

程式執行完畢時間{}

林姿岑 S05490061 \n

***********************************************************************************
""".format(datetime.datetime.now()))

input('Please enter any key to exit...')
print()
















