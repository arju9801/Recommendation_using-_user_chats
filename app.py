from flask import Flask, redirect, url_for, request, jsonify
import fetch_products as fp

import recommender as rc

app = Flask(__name__)

@app.route("/getSomething",methods=['POST'])
def getSomething():
	text = request.json['text']
	print(text)
	products,specs = fp.get_products(text)
	print(products)
	print(specs)
	arr = rc.get_recommendations(products[0], specs)
    
	return arr

if __name__ == "main":
	#app.debug = False
	port = int(os.environ.get('PORT',33507))
	#app.run(host='127.0.0.1:5000',debug=True)
	waitress.serve(app,port=port)