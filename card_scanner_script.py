#import time stuffs
import time
import datetime
import os
import sys

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
swipe = "swipe"
name = "John Doe"
cardNum = "8675309"
idnum = "123"
slash = 1
space = 1
carrot = 1
outPut = "foo"

os.system("stty -echo")
swipe = raw_input()
os.system("stty echo")
#while not exiting
while(swipe != ""):
	#check if read is succesfull
	if(swipe[1] == 'B'):
		#parse input to multiple strings
		cardNum = swipe[2:18]
		slash = swipe.find('/')
		space = swipe.find('  ') + 2
		carrot = swipe.find(' ^')
		name = swipe[slash  + 1:space] + swipe[19:slash]
		idnum = swipe[carrot+14:carrot+23]
		#output that in the format for the file
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		outPut = "Name:" + '\t' + name + '\t' + "Card Number:" + '\t' + cardNum + '\t' + "ID number:"+ '\t' + idnum + '\t' + "Time:" + '\t' + st + '\n'
		fo.write(outPut)
		raw.write(swipe)
		print("Welcome " + name + "!")
	elif(swipe[1] == 'E'):
		#output error message
		print("Error: Please reswipe card")	   
	#next swipe
	os.system("stty -echo")
	swipe = raw_input()
	os.system("stty echo")
#end while
#close output file
fo.close()
#end program
