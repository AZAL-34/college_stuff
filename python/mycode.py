import sys, time

def typing(stringus, delay, newline):
  for x in range(0, len(stringus)):
    sys.stdout.write(stringus[x])
    time.sleep(delay)
  if newline == True:
    sys.stdout.write("\n")
    
while True:
  typing("H A ", 0, False)