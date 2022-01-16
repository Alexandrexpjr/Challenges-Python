# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# This idea of switcher was inspired in this article: https://jaxenter.com/implement-switch-case-statement-python-138315.html
def my_switcher(n, case):
  switcher = {
    'even': int(n / 2), # Just to avoid decimal cases
    'odd': 3*n + 1,
  }
  return switcher[case]

def get_chain(n):
  current_number = n
  chain = [n]
  while(chain[-1] != 1): # while the last number isn't one
    if(current_number % 2 == 0):
      current_number = my_switcher(current_number, 'even')
      chain.append(current_number)
    else:
      current_number = my_switcher(current_number, 'odd')
      chain.append(current_number)
  return {'chain': chain, 'number': n, 'size': len(chain)} # Some extra info to simplify the work later

print(get_chain(13)) # It worked

def get_longest_chain(max_number):
  biggest_chain = {'size': 0}
  for number in range(1, max_number):
    current_chain = get_chain(number)
    if(current_chain['size'] > biggest_chain['size']):
      biggest_chain = current_chain
  return biggest_chain['number']

print(get_longest_chain(1000000)) # 837799 
# Correct
