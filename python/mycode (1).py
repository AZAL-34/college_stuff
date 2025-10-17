import sys, time, random

def typing(stringus, delay, newline):
  for x in range(0, len(stringus)):
    sys.stdout.write(stringus[x])
    time.sleep(delay)
  if newline == True:
    sys.stdout.write("\n")
    
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
  typing((alphabet[random.randint(0,25)]), 0, False)