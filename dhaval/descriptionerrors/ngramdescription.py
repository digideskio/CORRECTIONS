# -*- coding: utf-8 -*-
"""
ngram.py
To generate words having unique ngrams.   
"""
import sys, re
import codecs
import string
import datetime
from math import log

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def triming(lst):
	output = []
	for member in lst:
		member = member.strip()
		output.append(member)
	return output

def ngrams(input, n):
	output = []
	if n >= len(input): # Removing whole word entries.
		pass
	else:		
		for i in range(len(input)-n+1):
			output.append(input[i:i+n])
	return output

def getngrams(words,nth):
	ngr = []
	for word in words:
		ngr += ngrams(word,nth)
	ngr = set(ngr)
	return ngr

def getwords(data,dict,lineinput=False):
	words = []
	if not lineinput:
		print len(data), 'lines to read and process'
		if dict in ['ap90','ap']:
			entries = re.split(r'[<][P][>]',data)
		elif dict in ['vcp','pw','pwg']:
			entries = re.split('[<]H[1I][>]',data)
		print len(entries), 'entries total'
		for line in entries:
			line = line.strip()
			line = line.lstrip('<HI>')
			line = re.sub('\[.*\]','',line)
			line = re.sub('[0-9]','',line)
			line = line.replace('^','')
			line = line.replace("\\","")
			if dict in ['skd','vcp']:
				parts = [line]
			elif dict in ['ap','ap90','ae']:
				parts = re.findall('\{#([^#]*)#\}',line)
			elif dict in ['pwg']:
				parts = re.findall('\{#([^}]*)[#]*\}',line)
			elif dict in ['pw']:
				parts = re.findall('#\{([^}]*)\}',line)
			for part in parts:
				words += re.split('\W+',part)
	else:
		line = data
		line = line.strip()
		line = line.lstrip('<HI>')
		line = re.sub('\[.*\]','',line)
		line = re.sub('[0-9]','',line)
		line = line.replace('^','')
		line = line.replace('\\','')
		if dict in ['skd','vcp']:
			parts = line
		elif dict in ['ap','ap90','ae']:
			parts = re.findall('\{#([^#]*)#\}',line)
		elif dict in ['pwg']:
			parts = re.findall('\{#([^}]*)[#]*\}',line)
		elif dict in ['pw']:
			parts = re.findall('#\{([^}]*)\}',line)
		for part in parts:
			words += re.split('\W+',part)
		
	words = [member for member in words if len(member) > 1]
	words = set(words)
	return words

if __name__=="__main__":
	# Creating base ngrams
	# '../../../Cologne_localcopy/skd/skdtxt/skd.txt' for SKD and '../../../Cologne_localcopy/vcp/vcptxt/vcp.txt' for VCP.
	basefilename = '../../../Cologne_localcopy/'+sys.argv[1]+'/'+sys.argv[1]+'txt/'+sys.argv[1]+'.txt'
	fin1 = codecs.open(basefilename,'r','utf-8')
	data1 = fin1.read()
	fin1.close()
	print "Scraping words from", basefilename
	basewords = getwords(data1,sys.argv[1])
	print len(basewords), "Words scraped."
	print "Generating bigrams."
	basebigrams = getngrams(basewords,2)
	print len(basebigrams), "bigrams generated."
	print "Generating trigrams."
	basetrigrams = getngrams(basewords,3) 
	print len(basetrigrams), "trigrams generated."

	testfilename = '../../../Cologne_localcopy/'+sys.argv[2]+'/'+sys.argv[2]+'txt/'+sys.argv[2]+'.txt'
	fin2 = codecs.open(testfilename,'r','utf-8')
	data2 = fin2.readlines()
	fin2.close()
	print "Printing the files with abnormal bigrams and trigrams on screen."
	fout = codecs.open(sys.argv[2]+'vs'+sys.argv[1]+'errors.txt','w','utf-8')
	counter = 0
	positives = 0
	for line in data2:
		counter += 1
		originalline = line.strip()
		line = line.strip()
		wordinline = getwords(line,sys.argv[2],True)
		linebigrams = getngrams(wordinline,2)
		linetrigrams = getngrams(wordinline,3)
		if len(linebigrams.difference(basebigrams)) > 0:
			positives += 1
			print line.encode('utf-8')
			diff = linebigrams.difference(basebigrams)
			print str(counter), diff
			fout.write(originalline+'\n')
			fout.write(str(counter)+':'+','.join(list(diff))+'\n')
		elif len(linetrigrams.difference(basetrigrams)) > 0:
			positives += 1
			print line.encode('utf-8')
			diff1 = linetrigrams.difference(basetrigrams)
			print str(counter), diff1
			fout.write(originalline+'\n')
			fout.write(str(counter)+':'+','.join(list(diff1))+'\n')
	fout.close()
	print str(positives), 'suspicious entries found in', sys.argv[2]
	