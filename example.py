import sys
from bjorklund import bjorklund

try:
  steps = int(sys.argv[1])
  pulses = int(sys.argv[2])
except Exception:
  print("usage: python bjorklund.py <STEPS> <PULSES>")
else:  
  print(bjorklund(steps, pulses))
