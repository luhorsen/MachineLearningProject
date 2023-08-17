
# 请在此输入您的代码
a1, b1, c1 =input().split('/')
def runnian(year):
  if (year%4 == 0 and year%100 != 0) or year % 400 == 0:
    return True
list1= []
def fin(a1,b1,c1):
  a = int(a1)
  b = int(b1)
  c = int(c1)
  if a >= 60:
    a = a+1900
    if runnian(a):
      month = [31,29,31,30,31,30,31,31,30,31,30,31,]
      if  0<b<=12 and 0< c <= month[b-1]:
        list1.append('19'+a1+'-'+b1+'-'+c1)
    else:
      month = [31,28,31,30,31,30,31,31,30,31,30,31,]
      if  0<b<=12 and 0< c <= month[b-1]:
        list1.append('19'+a1+'-'+b1+'-'+c1)                                              
  else:
    a = a+2000
    if runnian(a):
      month = [31,29,31,30,31,30,31,31,30,31,30,31,]
      if  0<b<=12 and 0< c <= month[b-1]:
        list1.append('20'+a1+'-'+b1+'-'+c1)
    else:
      month = [31,28,31,30,31,30,31,31,30,31,30,31,]
      if  0<b<=12 and 0< c <= month[b-1]:
        list1.append('20'+a1+'-'+b1+'-'+c1)
fin(a1,b1,c1) 
fin(c1,b1,a1)
fin(c1,a1,b1)
list1=list(set(list1))
list1.sort()  # 默认reverse=False升序
for i in list1:
  print(i)
