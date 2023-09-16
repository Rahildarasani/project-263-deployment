from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")

def main():

	return render_template("index.html")

@app.route("/" , methods=['POST'])

def maths_operation():
	
	text = request.form['text']

	result = 'https://newton.now.sh/api/v2//'+operation+'/'+ equation
	data = requests.get(result).json()
	print("Expression for your given equation: ",equation)
	print("Result of given equation: " ,data)

if __name__ == "__main__":
	app.run()