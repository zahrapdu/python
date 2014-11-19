__author__ = 'admin'
def function_num(list):
  sum=0.0
  i=0
  for i in range(len(list)):
     sum=sum+list[i]
  min=sum/len(list)
  s=sorted(list)

      l=len(s)/2
      h=len(s)/2-1
      md=(s[l]+s[h])/2
  else:
      b=len(s)/2
      md=s[b]
  N=(sum-min)/len(list)

  print min
  print md
  print N
if __name__=='__main__':
 print function_num([12,6,7,3,15,10,18,5])
 print function_num([5,6,7,88,15,6,18,2])
 print function_num([12,6,7,3,5])
 print function_num([12,6,5,10,18,5])