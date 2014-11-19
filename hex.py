__author__ = 'admin'
def Hex_number(x):
 list=[]
 i=0
 while(x!=0):
  m=x%16
  if  m<10:
    list.append(m)
  if  m==10:
    list.append('A')
  if  m==11:
    list.append('B')
  if  m==12:
    list.append('C')
  if  m==13:
    list.append('D')
  if  m==14:
    list.append('E')
  if m==15:
    list.append('F')
  x=x/16
 i=i+1
 list.reverse()
 for j in range(len(list)):
     print list[j],
if __name__=='__main__':
 print Hex_number(26)
 print Hex_number(196)
 print Hex_number(75)
 print Hex_number(324)

