#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    #if n %2 != 0 :
    #    print ("wierd")
    #else :
    #    if n>1 or n<6 :
    #        print ("Not Weird")
    #    elif n>7 or n <21:
    #        print ("Weird")
    #    elif n>20 :
    #        print ("Not Weird")

    if n % 2 == 1:
        print("Weird")
    elif n % 2 ==0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
