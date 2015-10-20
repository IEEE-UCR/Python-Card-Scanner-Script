#import time stuffs
import time
import datetime
import os
import sys

def swipeLinux():
	os.system("stty -echo")
	input = raw_input()
	os.system("stty echo")
	return input

def genEmail(fname, lname, digits):
	address = fname[0]
	lnamelength = len(lname)
	i = 0
	added = 0
	while i < 0 && i < lnamelength:
		 

#open output file
fo = open("parsed.txt", "w")
if(fo.closed):
	print "Error: file failed to open."
	sys.exit()
raw = open("raw.txt", "w")
if(raw.closed):
   print "Error: file failed to open."
   sys.exit()

#declare and initalize variables
track1 = "t1"
track2 = "t2"
fname = "John"
lname = "Doe"
cardNum = "8675309"
idnum = "123"
slash = 1
space = 1
carrot = 1
outPut = "foo"

#takes care of os dependent stuff
if(sys.platform == 'linux2'):
	track1 = swipeLinux()
	track2 = swipeLinux()
	
#while not exiting
while(track1 != ""):
	#check if read is succesfull
	if(track1[1] == 'B'):
		#parse input to multiple strings
		cardNum = track1[2:18]
		slash = track1.find('/')
		space = track1.find('  ') + 2
		carrot = track1.find(' ^')
		fname = track1[slash  + 1:space] 
		lname = track1[19:slash]
		idnum = track1[carrot+14:carrot+23]
		#output that in the format for the file
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		print("Welcome " + fname + " " + lname + "!")
		digits = input("Please input the three digits at the end of your netID: ")
		email
		outPut = "Name:" + '\t' + name + '\t' + "Card Number:" + '\t' + cardNum + '\t' + "ID number:"+ '\t' + idnum + '\t' + "Time:" + '\t' + st + '\n'
		fo.write(outPut)
		raw.write(track1 + track2)
	elif(track1[1] == 'E'):
		#output error message
		print("Error: Please reswipe card")	   
	#next swipe
	if(sys.platform == "linux2"):
        	track1 = swipeLinux()
        	track2 = swipeLinux()
#end while
#close output file
fo.close()
raw.close()
#end program
