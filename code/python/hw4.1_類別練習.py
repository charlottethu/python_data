#**********************************************
# Name: 林姿岑
# Class: 資管系三年級
# SID: s05490061
# Program Name: hw4_1.py
# Function: 需宣告下面四個類別
#           (1) 圓形類別:需記錄半徑，並宣告面積與周長計算的方法。
#           (2) 長方形類別:需記錄長和寬，並宣告面積與周長計算的方法。
#           (3) 梯形類別:需記錄上底、下底與高，並宣告面積計算的方法。
#           (4) 三角形類別:需記錄底與高，並宣告面積計算的方法。
# Homework: No.4
# Limitations: (1).尚無發現
# Date: 2018/12/09
#**********************************************


#---建立圓形類別---#
class Cir():
    def __init__(self, name, a):#定義函式init
        self.name = name   #將name儲存到self.name
        self.a = a   #將a儲存到self.a
    def length(self):#定義函式length計算周長
        return 2*3.14*self.a
    def area(self):#定義函式area計算面積
        return 3.14*self.a*self.a

c1 = Cir('圓形物件一', 5)#宣告一個類別圓形的物件
c2 = Cir('圓形物件二', 12.5)#宣告一個類別圓形的物件
print()   # 空一行
print(c1.name, '\n\t面積: ', c1.area() ,'平方公分', '\n\t周長: ', c1.length() ,'公分')
#印出圖形名，面積和周長
print(c2.name, '\n\t面積: ', c2.area() ,'平方公分', '\n\t周長: ', c2.length() ,'公分')

print()# 空一行

#---建立長方形類別---#
class Rec():
    def __init__(self, name, a, b):#定義函式init
        self.name = name#將name儲存到self.name
        self.a = a #將a儲存到self.a
        self.b = b #將b儲存到self.b
    def length(self): #定義函式length計算周長
        return 2*(self.a+self.b)
    def area(self): #定義函式area計算面積
        return self.a*self.b
    
r1 = Rec('長方形物件一', 6, 100)#宣告一個類別長方形的物件
r2 = Rec('長方形物件二', 13, 62)#宣告一個類別長方形的物件
print(r1.name, '\n\t面積: ', r1.area() ,'平方公分', '\n\t周長: ', r1.length() ,'公分')
#印出圖形名，面積和周長
print(r2.name, '\n\t面積: ', r2.area() ,'平方公分', '\n\t周長: ', r2.length() ,'公分')
print()  # 空一行  

#---建立梯形類別---#
class Tra():
    def __init__(self, name, a, b, c):#定義函式init
        self.name = name #將name儲存到self.name
        self.a = a #將a儲存到self.a
        self.b = b #將b儲存到self.b
        self.c = c #將c儲存到self.c
    def area(self):#定義函式area計算面積
        return (self.a + self.b)*self.c /2

ta1 = Tra('梯形物件一', 15, 20, 6)#宣告一個類別梯形的物件
ta2 = Tra('梯形物件二', 8 ,60, 18)#宣告一個類別梯形的物件
print(ta1.name, '\n\t面積: ', ta1.area() ,'平方公分')
#印出圖形名，面積
print(ta2.name, '\n\t面積: ', ta2.area() ,'平方公分')
print()# 空一行  
    
#---建立三角形類別---#
class Tri():
    def __init__(self, name, a, b):#定義函式init
        self.name = name#將name儲存到self.name
        self.a = a#將a儲存到self.a
        self.b = b#將b儲存到self.b
    def area(self):#定義函式area計算面積
        return self.a * self.b/2


t1 = Tri('三角形物件一', 13, 8)#宣告一個類別三角形的物件
t2 = Tri('三角形物件二', 21.5, 18)#宣告一個類別三角形的物件
print(t1.name, '\n\t面積: ', t1.area() ,'平方公分')#印出圖形名，面積
print(t2.name, '\n\t面積: ', t2.area() ,'平方公分')#印出圖形名，面積

print()   # 空一行
input('Please enter any key to exit...')
print()   # 空一行
