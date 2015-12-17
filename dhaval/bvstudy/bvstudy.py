# -*- coding: utf-8 -*-
""" bvstudy.py

To generate list of words having 'b' in them and having 'v' in some other dictionary.
To normalise and study of Bengal influenced dictionaries.

See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/181 Point 14  
"""
import sys, re
import codecs
import string
import datetime

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def triming(lst):
	output = []
	for member in lst:
		member = member.strip()
		output.append(member)
	return output

# Create a list of (word,dictionarylist) tuple.
def sanhw1():
	fin = codecs.open('../../sanhw1/sanhw1.txt','r','utf-8')
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip() # 'aMSakalpanA:CAE,CCS,MD,MW,PD,PW'
		split = line.split(':') # ['aMSakalpanA', 'CAE,CCS,MD,MW,PD,PW']
		word = split[0] # 'aMSakalpanA'
		dicts = split[1].split(',') # ['CAE','CCS','MD','MW','PD','PW']
		output.append((split[0],dicts)) # ('aMSakalpanA', ['CAE','CCS','MD','MW','PD','PW'] )
	return output
# Read data in sanhw2.txt format
def sanhw2(inputfile):
	fin = codecs.open(inputfile,'r','utf-8')
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip()
		split = line.split(':') # ['aMSakalpanA', 'CAE;4,CCS;4,MD;4,MW;21,PD;50,PW;9']
		word = split[0] # 'aMSakalpanA'
		dictswithlnum = split[1].split(',') # ['CAE;4','CCS;4','MD;4','MW;21','PD;50','PW;9']
		dicts = []
		lnums = []
		for dictwlnum in dictswithlnum:
			[dict,lnum] = dictwlnum.split(';')
			dicts.append(dict) # ['CAE','CCS','MD','MW','PD','PW']
			lnums.append(lnum) # [4,4,4,21,50,9]
		output.append((word,dicts,lnums))
	return output
print "Creating headword data of sanhw2.txt"
sanhw2 = sanhw2('../../sanhw2/sanhw2.txt','r','utf-8')
hw = [word for (word,dicts,lnums) in sanhw2]	
print "Created headword data of sanhw2.txt"
def getbasewords(basedict):
	global sanhw2
	headwithdicts = sanhw2
	basewords = []
	otherwords = []
	for (word,dicts,lnums) in headwithdicts:
		if basedict in dicts:
			basewords.append(word)
		else:
			otherwords.append((word,dicts,lnums))
	return [basewords,otherwords]

def dictlnumback(dicts,lnums):
	output = ''
	for i in xrange(len(dicts)):
		output += ","+dicts[i]+";"+lnums[i]
	output = output.strip(',')
	return output
def generatebasefiles():
	fout1 = codecs.open('bwords.txt','w','utf-8')
	fout2 = codecs.open('vwords.txt','w','utf-8')
	fout3 = codecs.open('bvwords.txt','w','utf-8')
	for (word,dicts,lnums) in sanhw2:
		if re.search('b',word) and re.search('v',word):
			fout3.write(word+":"+dictlnumback(dicts,lnums)+"\n")
		elif re.search('b',word):
			fout1.write(word+":"+dictlnumback(dicts,lnums)+"\n")
		elif re.search('v',word):
			fout2.write(word+":"+dictlnumback(dicts,lnums)+"\n")
	fout1.close()
	fout2.close()
	fout3.close()
	
if __name__=="__main__":
	#generatebasefiles()
	