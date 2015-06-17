#!/usr/bin/python 
"""
	Author: Jia Wei
	Last Updated: 17/6/2015 15:32:34 SGT

This python script first obtains the data from a text file containg the intervals for the individual vowels. It processses the databy compiling all the xmin and xmax points into a list, before     calculating its mean vocalic length of each vowel and standard deviation.

usage: python calculate_vocalic_.py inputfile phone
e.g. python calculate_vocalic.py normal_a.txt a  

"""

import sys,random,math,os,glob,re

#parse input file
try:
    infile,phone=sys.argv[1:]
except:
    print "DIED"
    sys.exit(-1)

fin=open(infile,'rt')
data=fin.read()

data=str(data)
if len(re.findall("xmin = +\d+.\d+",data))!=0:
	xmin=re.findall("xmin = +\d+.\d+",data)	

if len(re.findall("xmax = +\d+.\d+",data))!=0:
	xmax=re.findall("xmax = +\d+.\d+",data)


no_ofxmin=len(xmin)
strxmin=str(xmin)
start=re.findall("\d+.\d+",strxmin)

no_ofxmax=len(xmax)
strxmax=str(xmax)
end=re.findall("\d+.\d+",strxmax)

start=re.findall("\d+.\d+",strxmin)
end=re.findall("\d+.\d+",strxmax)
sumofxmin=0
sumofxmax=0

listxmin=[float(i) for i in start]
listxmax=[float(i) for i in end]


start=str(start)
end=str(end)	

#splits the list of numbers into individual strings, before converting them into floating points and finding the sum 
for num in start.split(', '):
	num=num.translate(None,"[],\'")
	sumofxmin += float(num)

for xmaxnum in end.split(', '):
	xmaxnum=xmaxnum.translate(None, "[],\'")
	sumofxmax += float(xmaxnum)


lst = [i-j for i, j in zip(listxmax,listxmin)]



if no_ofxmax == no_ofxmin == len(lst):
    noofvowels=no_ofxmin

#find xmax-min which is the sum of all the intervals, and the total length of the vowels
total_lengthofvowels= sumofxmax-sumofxmin

#take mean vocalic length
meanvocaliclength=total_lengthofvowels/noofvowels

#take standard variance of vocalic length
for i in range(0,len(lst)):
    standardvariance=0
    standardvariance+=(i-meanvocaliclength)**2
    standardvariance=standardvariance/noofvowels

#takes the square root of the variance, the result is the standard deviation
standarddeviation=standardvariance**0.5

#print mean and standard deviation
print "The mean vocalic length of the phone %s is %f." %(phone,meanvocaliclength) 
print "The standard deviation for the phone %s is %f." %(phone,standarddeviation)


fin.close()

