#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from flask import render_template, Flask, request, url_for
from apps import app

from google.appengine.ext import db

class Photo(db.Model):
	photo = db.StringProperty()

@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html", all_list=Photo.all())

@app.route('/upload', methods=['POST'])
def upload_db():
	upload_data = Photo()
	upload_data.photo = request.form['grim'] #Blob이란 형태로 바꿈. 액자를 만듦
	upload_data.put() #db에 저장

	#url = url_for("shows", key = upload_data.key()) #shows 함수를 실행시켜 변수 url에 url 형식으로 저장

	#return render_template("upload.html", url = url)
	
	return render_template("upload.html", all_list = Photo.all())
	#return render_template("upload.html", all_list = Photo.all()) #사진을 위한 url을 출력

"""
@app.route('/show/<key>') # appspot/show/key에 저장된 이미지로 접속하면~
def shows(key):
	uploaded_data = db.get(key) #이미지를 변수에 저장 
	return app.response_class(uploaded_data.photo) #uploaded_data를 위한 url를 제작
"""
