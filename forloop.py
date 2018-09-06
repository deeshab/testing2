#!/usr/bin/env python3
#rzhang26:20171027:HW7A:forloop.py

#Q2a
s0 = 'computing'
s1 = 'introduce'
d0 = {'a ':3,'b ':5,'c ':2}

#Q2b
for i in s0:
	print(i)

#Q2c
for i in range(len(s0)):
	print(i+2, s0[i])

#Q2d
for i in range(len(s1)):
	print(s1[i] + " " + s0[i])

for i in d0.keys():
	j = d0[i]
	l = ""
	for k in range(j):
		l = l + i	
	print(l)
