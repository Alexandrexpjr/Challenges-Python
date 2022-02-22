"""25 - The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

def get_first_fibonacci_number_with_n_digits(n):
  fibonacci_numbers = [1, 1, 2]
  while (len(str(fibonacci_numbers[-1])) < n):
    nextNumber = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(nextNumber)
  return len(fibonacci_numbers) #The last index will be length - 1, and the algorithm stops when some number reaches that number, BUT the challenge call index the nth number regardless of index 0

print(get_first_fibonacci_number_with_n_digits(1000)) # 4782


# Correct