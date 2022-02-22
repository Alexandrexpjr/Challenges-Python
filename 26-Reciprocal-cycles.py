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

def check_n_recurring_cycle(n):
  n_set = set()
  current_cycle_size = 0
  value = 1
  while(value != 0 ):
    value *= 10
    value %= n
    if value in n_set:
      break
    else: 
      current_cycle_size += 1
      n_set.add(value)
  return { 'number': n, 'size': current_cycle_size }

def find_longest_recurring_cycle_under_d(d):
  number_with_longest_cycle = 0
  cycle = 0
  for number in range(d, 0, -1):
    if (cycle >= number): break
    get_cycle = check_n_recurring_cycle(number)
    if(get_cycle['size'] > cycle):
      cycle = get_cycle['size']
      number_with_longest_cycle = number
  return print(f'The number {number_with_longest_cycle} has the longest recurring cycle, which is {cycle}')

find_longest_recurring_cycle_under_d(1000) # The number 983 has the longest recurring cycle, which is 982

# Correct