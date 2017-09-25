# Samantha Ngo
# Softdev1 - pd7
# HW04 -- Fill Up Yer Flask
# 2017-09-24

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello?"

@app.route('/sweets')
def food():
    return 'ice cream'
	
@app.route('/frustration')
	return "This is frustrating. What happens next?"

@app.route('/works')
	return "You'll see this if it works."

if __name__ == "__main__":
	app.debug = True
	app.run()

''' NOTES
The following code:
	@app.route("/pop")
	def people():
		return "Pop!"
	app.people()

	@app.route("/food")
	def food():
		return "Chocolate"
	app.food()
...returns the following error: 
	"AttributeError: 'Flask' object has no attribute 'pop'
'''
	
	
