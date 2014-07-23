from flask import render_template, Flask, request
#from apps import app

app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	get = None
	post = None
	
	if request.args:
		get = request.args['text_get']
		b = "http://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ie=utf8&query="+get+"&x=0&y=0"
	if request.form:
		post = request.form['text_post']

	return render_template("index.html", variable_get = b, variable_post = post)

if __name__ == "__main__":
	app.run(port = 5010)