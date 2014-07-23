#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)

"""
print data
print

data_print = json.dumps(data, sort_keys=True, indent=4)
print data_print	# 단순 보기 좋게 출력하기 위함
print
"""

print "MEM_NUM" + "   " + "Age" + "       " + "Job" + "	        " + "MEM_CODE" + "     " + "etc"
#print "MEM_NUM" + "Age" + "Job" + "MEM_CODE" + "etc"

for i in range(len(data['data'])):
	element_i = data['data'][i]
	etc = ""
	if element_i['age'] >= 50 and element_i['job'] == "Programmer":
		etc = "Master Old"
	elif element_i['age'] >= 50:
		etc = "Old"
	elif element_i['job'] == "Programmer":
		etc = "Master"
	else:
		etc = ""

	print "%5.1d" % (element_i['MEM_NUM']) + "%8.2d" % element_i['age'] + "%13s" % element_i['job'] + "%15.10d" % element_i['MEM_CODE'] + "    " + "%2.10s" % etc
