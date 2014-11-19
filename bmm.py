__author__ = 'admin'
def Bmm_number(x,y):
 if y==0:
  return x
 else:
  return Bmm_number(y,x%y)
if __name__=='__main__':
 print Bmm_number(8,12)
 print Bmm_number(7,14)
 print Bmm_number(5,0)
 print Bmm_number(90,3)
