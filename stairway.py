#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
#sys.stdin = open('stairway_input_0.txt')
#sys.stdout = open('stairway_output_0.txt', 'w')

N = int(input().strip())

B = 0


# INSERT YOUR CODE HERE

for i in range (0, N+1, 1):
    B = B + i


print(B)

sys.stdout.close()
