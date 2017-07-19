# 計算
1129+2344
400-330
2800*1.08
1920/12
(40+50)*3-50
40+50*3-50
255%3
255%7
2**3
4**4
(4+5j)-(3-4j)
1j**2

# 変数
# 変数=値
tax=0.08
price=120
suzuki_telephone='090-1234-5678'
price*tax
120*0.08

# 予約語の表示
import keyword
keyword.kwlist

# 比較
# > >= < <= == !=
34>22
34<22
apple=15
apple==15

# 数値型
34+56
number=55
5+3.4
5/2
complex=5+5j
complex+(3+1j)

# 文字列型
'happy birthday!'
message="おめでとう！"

# 複数行の文字列
'''
Sunday
Monday
tuesday
'''
'thunder'+'bolt'
'hunter'*2
text='hello'
text.upper()
word='maintenance'
word.count('n')

# 論理型
46<49
46>49

# リスト型
Agroup=['kazu','gorou']
Bgroup=['syun','haruka']
Agroup
Agroup.append('dai') # リストに追加
Agroup
Agroup.remove('kazu') # リストから削除
Agroup
Agroup.sort() # リストの順番を変更
Agroup
testResult=[87,55,99,50,66,78]
testResult.sort()
testResult

# 辞書型
activities={'Monday':'バスケ','Tuesday':'自転車','Wednesday':'軽音','Friday':'水泳'}
activities['Tuesday']
activities['Friday']
activities.keys()
activities.values()

# タプル型
tuple=('apple',3,90.4)
print(tuple)
list=['ミント','チョコ','ストロベリー','バニラ']
print(list)
list[0]='ラムレーズン'
print(list)
tuple=('ミント','チョコ','ストロベリー','バニラ')
tuple[0]='ラムレーズン'
print(tuple)
diary={}
key=('kamata','08-01')
diary[key]='70kg'
print(diary)
diary['kamata','08-01']
diary={}
key=['nakata','08-01']
diary[key]='50kg'

# 集合型
candy={'delicious','fantastic'}
print(candy)
candy=set('delicious')
print(candy)
flavor=['apple','peach','soda']
candy=set(flavor)
candy
candy.update(['grape'])
candy

# 集合型 重複を削除
flavor=['apple','soda','chocolate','apple','grape','grape','soda']
flavor_set=set(flavor)
print(flavor_set)
flavor=list(flavor_set)
print(flavor)

# 集合型 データ同士の計算
# <= >= | & - ^
flavor_A={'apple','peach','soda'}
flavor_B={'apple','soda','chocolate'}
flavor_A-flavor_B
flavor_A&flavor_B

# 条件分岐
age=29
if(18<=age):
  print('チケットを売る')
age=15
if(18<=age):
  print('チケットを売る')
else:
  print('チケットを売ることができません')
if(60<=age):
  print('チケットは1000円です')
elif(18<=age<=59):
  print('チケットは1800円です')
else:
  print('チケットを売ることができません')
pointcard=True
count=5
if(pointcard==True):
  if(count==5):
    print('いつもありがとうございます。今回は1000円です。')
if((pointcard==True)and(count==5)):
  print('いつもありがとうございます。今回は1000円です。')
if(age<18):
  print('チケットを売ることはできません。')
elif((60<=age)or((pointcard==True)and(count==5))):
  print('チケットは1000円です。')
else:
  print('チケットは1800円です。')

# 繰り返し
for count in range(3):
  print('繰り返します')
  print(count)
word='ninja'
for chara in word:
  print(chara)
musicList=['metal','rock','pop','anime']
for music in musicList:
  print('now playing...'+music)
menu={'ラーメン':500,'チャーハン':400,'餃子':200}
for order in menu:
  print(order)
  print(menu[order]*1.08)
counter=0
while(counter<5):
  print(counter)
  counter=counter+1
power=2
while(True):
  print('パンチ')
  print('キック')
  print('必殺奥義')
  power=power-1
  if(power==0):
    break
for number in range(3):
  print('あ')
  print('い')
  continue
  print('う')

# 関数
def washingMachine():
  print('給水')
  print('洗濯')
  print('脱水')
washingMachine()
def washingMachine(mode):
  print('給水')
  if(mode=='soft'):
    print('やさしく洗濯')
  elif(mode=='hard'):
    print('はげしく洗濯')
  else:
    print('ふつうに洗濯')
  print('脱水')
washingMachine('hard')
def area(radius):
  result=radius*radius*3.14
  return result
area(5)
len('thunderbolt')
animal=['dog','cat','horse']
len(animal)
max(40,12,44)
min(430,323,10)
max('test')
min('test')
sorted('test')
sorted([100,21,340])
type(power)
type(animal)
dir(power)
dir()

# 例外処理
try:
  prin('例外')
except:
  print('例外をキャッチ')
try:
  prin('例外')
except Exception as e:
  print(e.args)

# クラス
class fruit:
  color='red'
  def taste(self):
    return 'delicious'
apple=fruit()
apple.color
apple.taste()
# オブジェクト
color='green'
color.count('e')
color.upper()
class staff:
  def salary(self):
    return '10000yen'
yamamoto=staff()
yamamoto.salary()
class staff:
  bonus=30000
  def salary(self):
    salary=10000+self.bonus
    return salary
yamamoto=staff()
yamamoto.salary()
class staff:
  def __init__(self,bonus):
    self.bonus=bonus
  def salary(self):
    salary=10000+self.bonus
    return salary
yamamoto=staff(50000)
yamamoto.salary()

# 継承
class animalBaseClass:
  animallegs=4
  def walk(self):
    print('あるく')
  def cry(self):
    print('なく')
  def getLegsNum(self):
    print(self.animallegs)
class dogClass(animalBaseClass):
  def __init__(self):
    print('いぬです')
wanko=dogClass()
wanko.walk()
wanko.cry()
wanko.getLegsNum()
class birdClass(animalBaseClass):
  def __init__(self):
    print('とりです')
  def cry(self):
    print('ぴよぴよ')
piyo=birdClass()
piyo.walk()
piyo.cry()
class animalBaseClass():
  def __init__(self,num):
    self.animallegs=num
  def walk(self):
    print('あるく')
  def cry(self):
    print('なく')
  def getLegsNum(self):
    print(self.animallegs)
class snakeClass(animalBaseClass):
  def __init__(self,num):
    parent_class=super(snakeClass,self)
    parent_class.__init__(num)
    print('へびです')
nyoro=snakeClass(0)
nyoro.getLegsNum()

# 標準ライブラリ
import calendar
print(calendar.month(2015,7))
import calendar as cal
print(cal.month(2016,4))
from calendar import month,isleap
print(month(2017,5))
isleap(2012)
from datetime import date
date.today()
today=date.today()
today.strftime('%Y%m%d')
today.strftime('%Y/%m/%d')
today.strftime('%Y %B %d %a')
from datetime import datetime
datetime.now()
from datetime import datetime as dt
now=dt.now()
now.strftime('%Y-%m-%d %H:%m:%S')
from datetime import date,timedelta
today=date.today()
today
one_week=timedelta(days=7)
today+one_week
today-one_week

# ファイル操作
# r 読み取り w 書き込み a 追記 
open('null.txt','r')
file_object=open('text.txt','w')
file_object.write('this is sample!')
file_object.close()
file_object.write('this is sample!')
file_object=open('text.txt','w')
file_object.write('this is second!')
file_object.flush()
file_object=open('text.txt','r')
file_object.read()
file_object=open('text.txt','a')
file_object.write('add text!')
file_object.close()
file_object=open('text.txt','r+')
file_object.read()
file_object.write('add line!!\n')
file_object.close()
file_object.seek(0) # 読み込みはじめる場所を先頭にする
# withが終わるとclose
with open('text.txt','w') as file_object:
  file_object.write('Using With!!')

# 外部ライブラリ
# pillow
from PIL import Image
image=Image.open('image/1.jpg')
image.show()
r,g,b=image.split()
image2=Image.merge('RGB',(b,g,r))
image2.show()
image2.save('image/1_2.jpg')
baw=image.convert('1') # 白黒
baw=image.convert('L') # グレースケール
baw.show()
baw.save('image/1_3.jpg')
baw.save('image/1_4.jpg')
image.transpose(Image.ROTATE_90).show() # 90度回転させて表示
image.transpose(Image.ROTATE_90).save('image/1_5.jpg') # 90度回転させて保存

# 外部ライブラリ作成
import newyear
# パッケージ内のライブラリ読み込み フォルダ内に__imit__.pyが必要
import package.month
