#!/usr/bin/env python

#
# This software is a Python implementation of the algorithm by 
# E. Bjorklund and found in his paper, 
# "The Theory of Rep-Rate Pattern Generation in the SNS Timing System." 
# https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf
# 
# This implementation copyright (c) 2011 Brian House
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# 
# See <http://www.gnu.org/licenses/gpl.html> for details.
# 

def bjorklund(steps, pulses):
    steps = int(steps)
    pulses = int(pulses)
    if pulses > steps:
        raise ValueError    
    pattern = []    
    counts = []
    remainders = []
    divisor = steps - pulses
    remainders.append(pulses)
    level = 0
    while True:
        counts.append(divisor / remainders[level])
        remainders.append(divisor % remainders[level])
        divisor = remainders[level]
        level = level + 1
        if remainders[level] <= 1:
            break
    counts.append(divisor)
    
    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)         
        else:
            for i in xrange(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)
    
    build(level)
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[0:i]
    return pattern


if __name__ == "__main__":
    import sys
    try:
        steps = int(sys.argv[1])
        pulses = int(sys.argv[2])
    except Exception:
        print("usage: python bjorklund.py <STEPS> <PULSES>")
    else:  
        print(bjorklund(steps, pulses))
