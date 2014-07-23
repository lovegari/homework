#-*- coding: utf-8 -*-

import urllib
from xml.etree.ElementTree import parse

import webbrowser

xml = urllib.urlopen('http://rss.joins.com/joins_it_list.xml')	# 속보

tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기

number = 0
article = []
link = []

for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):	# item 태그를 모두 반복
		article.append(child.find("title").text)
		link.append(child.find("link").text)

for i in range(len(article)):
	print i+1, article[i]

print
question = raw_input("보고 싶은 뉴스 번호를 선택하셈요!ㅎ : ")
print

print article[int(question)-1]

url = link[int(question)-1]
print url
webbrowser.open(url)