# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
import re

def get_all_primes_below_n(n):
  primes = [2, 3]
  for number in range(3, n, 2):
    for prime in primes:
      if(number % prime == 0):
        break
      if(prime > number ** 0.5): 
        primes.append(number)
        break
  return primes

def insertList(ls, index, content):
  ls.insert(index, content)
  return ls

def getRegexes1():
  rege = []
  for n1 in range(10):
    for n2 in range(10):
      for n3 in [1, 3, 7, 9]:
        fix = f'([0-9])'
        curr = r''
        curr += str(n1) + str(n2) + str(n3)
        for i in range(len(curr)):
          newcurr = insertList(list(curr), i, fix)
          for i2 in range(len(newcurr)):
            newnewcurr =  insertList([*newcurr], i2, fix)
            for i3 in range(len(newnewcurr) - 1):
              ncr = insertList([*newnewcurr], i3, fix)
              s = ''.join(ncr)
              rege.append(s)
  return rege

def getRegexes2():
  rege = []
  for n1 in range(1, 10):
    for n2 in range(10):
      for n3 in range(10):
        for n4 in [1, 3, 7, 9]:
          fix = f'([0-9])'
          curr = r''
          curr += str(n1) + str(n2) + str(n3) + str(n4)
          for i in range(len(curr)):
            newcurr = insertList(list(curr), i, fix)
            for i2 in range(len(newcurr) - 1):
              newnewcurr =  insertList([*newcurr], i2, fix)
              s = ''.join(newnewcurr)
              rege.append(s)
              
  return rege

def getMatchs(n):
  primes = str(get_all_primes_below_n(n))
  regexes = getRegexes1()
  result = []
  for regex in regexes:
    matches = re.finditer(regex, primes)
    currMatch = []
    for match in matches:
      if (match.group(1) == match.group(2) == match.group(3)): currMatch.append(match)
    if (len(currMatch) > len(result)): result = currMatch
  
  return (result)

print(getMatchs(1000000)); # 121313

# Correct