from flask import Flask, render_template
import urllib2
import webbrowser
import json
from pprint import pprint



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	request_string = 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/sports/30?api-key=a1f2de9c74a24d2cf3f72d910ff68018:14:61296924'
	response = urllib2.urlopen(request_string)
	content = response.read()

	decoded = json.loads(content)
	articles = decoded['results']
	print '****************'
	

	return render_template('index.html', articles = articles)
	

	
	




	
	






if __name__ == '__main__':
	app.debug = True
	app.run()



