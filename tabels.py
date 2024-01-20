while(True):
 print("enter any numer to find its table from 1 to 10")
 print("you can press x to quit")
 num  = input(":")
 if num == 'x':
  break
 try:
  num  = float(num)
  table = [num*i for i in range(1,11)]
  print (table)
 except Exception as f :
  print('enter a valid input')
 
 except ValueError as f :
  print('enter a number')
 


 with open("tabels.txt","a")as f:
   f.write(str(table))
   f.write('\n')
