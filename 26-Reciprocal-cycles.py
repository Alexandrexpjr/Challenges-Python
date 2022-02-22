""" 26 - A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def get_longest_recurring_cycle(d):
  sequenceLength = 0
  for i in range(d, 0, -1):
    if (sequenceLength >= i):
      break
    foundRemainders = []
    value = 1
    while(value != 0 or len(foundRemainders) == 100):
      value *= 10
      value %= i
      foundRemainders.append(value)
    print(foundRemainders)
get_longest_recurring_cycle(100)


def get_cycle(number):
  pass

sequenceLength = 0
 
for i in range(1000, 0, -1):
  if (sequenceLength >= i):
    break
  foundRemainders = []
  value = 1
  position = 0

  while (foundRemainders[value] == 0 and value != 0):
    foundRemainders[value] = position
    value *= 10
    value %= i
    position += 1


  if (position - foundRemainders[value] > sequenceLength):
    sequenceLength = position - foundRemainders[value]

print(sequenceLength)