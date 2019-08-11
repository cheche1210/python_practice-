import sys
a = int(input())
b = a
for i in range(1,a+1):
    for j in range(b,1,-1):
        sys.stdout.write(' ')
    for j in range(1, 2*i):
        sys.stdout.write('*')
    print("")
        
 
  

 