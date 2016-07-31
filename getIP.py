#!Python2.7
#This script to get an IP address from a text file and wrrite it to another textfile

import re

#Step1: Get the opent the text file and get the text

hand=open('OptumIP.txt')

#Step2: create the regex to extract the IP

#GetIP=re.complie(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[1-9]{1,3}')



#Step3: find all the matches in the text file


for line in hand:
    line=line.rstrip()
    ip=re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[1-9]{1,3}',line)
    if len(ip)>0:
        print ip



#step4: Write the results to a text file
