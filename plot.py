#! /usr/bin/python

import sys
import matplotlib.pyplot as plt

if (len(sys.argv) < 2) : 
	print "Enter file to plot."
	print "Terminating..."
	sys.exit()
else:
	filename = sys.argv[1]
	print "Plotting file " + filename

log_file = open(filename, 'r')

time 	      = []
reference_0	= []
reference_1	= []
actual_0    = []
actual_1    = []
difference_0 = []
difference_1 = []

data = log_file.read().split('\n')
rows = []
for d in data:
	row = d.split('\t') 
	if len(row) > 1:
		time.append(row[0])
		reference_0.append(row[1])
		actual_0.append(row[3])
		reference_1.append(row[2])
		actual_1.append(row[4])
		# Reference - Real
		difference_0.append(float(row[3]) - float(row[4]))
		difference_1.append(float(row[1]) - float(row[2]))

plt.plot(time, actual_1)
plt.plot(time, reference_1)
plt.plot(time, difference_1)
plt.show()
