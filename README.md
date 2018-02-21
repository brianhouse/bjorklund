Euclidean Rhythms: Björklund's Algorithm in Python
==================================================

After encountering some [buzz](http://ruinwesen.com/blog?id=216) about it online, I read and was inspired by Godfried Toussaint’s paper, [“The Euclidean Algorithm Generates Traditional Musical Rhythms”](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf). In short, he demonstrates how many classic rhythms, particularly of African origin, can be described by a ubiquitous mathematical principle first documented by Euclid and even used for timing patterns in neutron accelerators.

However, while I found many implementations of the algorithm in various languages, all of the ones I tried (in Ruby, Python, Java, and Javascript) return inaccurate results! Trying 13 steps with 5 pulses was an easy way to break most of them. Luckily, Toussaint’s source, Björklund, provides C code in his paper [The Theory of Rep-Rate Pattern Generation in the SNS Timing System](https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf). I translated this into Python 3, and found the result to be elegant, efficient, and accurate.



### Copyright/License

Copyright (c) 2011 Brian House

This code is released under the MIT License and is completely free to use for any purpose. See the LICENSE file for details.
