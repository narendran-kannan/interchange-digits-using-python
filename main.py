

#Return nearest larger integer by Interchanging Digits in another input integer using Python by Narendran K

from itertools import permutations 
# Initialising empty list 
great = []

#getting Input1
a, b = map(int, input().split())
#a,b = raw_input().split()
input2 = b

strinput = str(a)
#Finding all possible permutations of the input
r = [perm for perm in permutations(strinput)]
#sorting the input
s = sorted(set(r))
#ierating the input and checking whether the permutation is greater than the input2   
for x in s:
  
  s = (''.join(x))
  if int(s) > input2:
    great.append(s)
    
#Printing the nearest largest number 

if not great:
  print (-1)
else:
  print (great[0])

 
   
    