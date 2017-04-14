'''1. Your task in this exercise is as follows:

Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.

Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK

   [][]      OK   ][][      NOT OK

   [[][]]    OK   []][[]    NOT OK
'''
import random

def random_stream(n):
   s = ""
   for i in range (0,n):
      if random.random()<=0.5:
         s+="]"
      else:
         s+="["
   return s

s = random_stream(random.randint(1,10))   #taking length of string from randint function of class random, length will be between 1 to 10
flag=0
count=0
print "string: "+s;
for i in s:
   if i == '[':
      count+=1
   else:
      count-=1
      if count<0:
         flag=1
         break
if count==0:
   print "Balanced"
else:
   print "Unbalanced"

   

