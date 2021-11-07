from flask import Flask, redirect, url_for, request, jsonify, make_response
from json import dumps
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
	arr = []
	if len(products)!=0: arr = rc.get_recommendations(products[0], specs)
	res = {"s.no":[],"item":[]}
	for it in range(0,len(arr)):
		res["s.no"].append(it)
		res["item"].append(arr[it])
	print(res)
	return jsonify(res)#make_response(dumps(arr))

if __name__ == "main":
	#app.debug = False
	port = int(os.environ.get('PORT',33507))
	#app.run(host='127.0.0.1:5000',debug=True)
	waitress.serve(app,port=port)