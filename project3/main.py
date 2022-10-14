import argparse
import random

parser = argparse.ArgumentParser(
  description = "Generate a secure, memorable password using the XKCD method")

parser.add_argument(
  '-w',
  '--words',
  type = int,
  default = 4,
  help = 'include WORDS words in the password (default=4)')

parser.add_argument(
  '-c',
  '--caps',
  type = int,
  default = 0,
  help = 'capitalize the first letter of CAPS random words (default 0)')

parser.add_argument(
  '-n', 
  '--numbers', 
  type = int, 
  default = 0,
  help = 'insert NUMBERS random numbers in the password (default=0)')

parser.add_argument(
  '-s',
  '--symbols',
  type = int,
  default = 0,
  help = 'insert SYMBOLS random symbols in the password (default=0)')

args = parser.parse_args()

words = args.words
caps = args.caps
numbers = args.numbers
symbols = args.symbols
pw = []
allSymbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]

try:
    caps = random.sample(range(1, 1 + words), caps)
except:
    caps = list(range(1, words + 1))


while words > 0:
    if words in caps:
        randomWord = random.choice(open("words.txt").read().split()).capitalize()
        pw.append(randomWord)
        words -=1
    else:
        randomWord = random.choice(open("words.txt").read().split())
        pw.append(randomWord)
        words -=1



for _ in range(numbers):
    pw.insert(random.randint(0, len(pw) + 1),
              str(random.randint(0,9)))

for _ in range(symbols):
    pw.insert(random.randint(0, len(pw) + 1),
              random.choice(allSymbols))

print("".join(pw))