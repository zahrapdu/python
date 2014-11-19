__author__ = 'admin'
def Day(x):
 m=x%365
 if m<186:
   moh=m/31
   day=m%31
 else:
  day=m%30
  moh=m/30
 if moh==0:
    moh=1
 if day==0:
     day=1
 print  moh,
 print  day
if __name__=='__main__':
 print Day(730)
 print Day(90)
 print Day(365)
 print Day(186)