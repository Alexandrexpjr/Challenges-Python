# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

number_letter_enum = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  100: 'hundred',
  1000: 'onethousand'
}

def count_letters_on_number(number):
  number_name = ''
  if(number < 20):
    number_name = number_letter_enum[number]
  if(number >= 20 and number < 100):
    number_name = number_letter_enum[int(str(number)[0] + '0')] + number_letter_enum[int(str(number)[1])]
  if(number >= 100):
    if(number % 100 == 0):
      number_name = number_letter_enum[int(str(number)[0])] + number_letter_enum[100] # This fixes the issue where the term 'and' appeared in the exact hundreds
    else:
      number_name = number_letter_enum[int(str(number)[0])] + number_letter_enum[100] + 'and' + count_letters_on_number(int(str(number)[-2:]))['name']
  return { 'number': number,'name': number_name, 'letters': len(number_name) }

# Worked. I know this could be better writed xD

def number_letter_count(limit):
  count = len(number_letter_enum[limit]) # Because the range will not apply the limit itself
  for number in range(limit):
    print(count_letters_on_number(number))
    count += count_letters_on_number(number)['letters']
  return count

print(number_letter_count(1000))

