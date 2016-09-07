import zmaps
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():

	return render_template('index.html')

@app.route("/query")
def query():
	
	try:
        	zid1 = request.args.get("zid1")
        	zid2 = request.args.get("zid2")
        	zid3 = request.args.get("zid3")
        	zroute, zembed = zmaps.genroute(zid1, zid2, zid3)
        	return render_template('index.html', zroute=zroute, zembed=zembed)
	
	except:
		oops = "Error"
		return render_template('index.html', oops=oops)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
