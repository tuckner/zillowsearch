import zmaps
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():

	return render_template('index.html')

@app.route("/", methods=['POST'])
def search():

	startloc = request.form.get("startloc")
	endloc = request.form.get("endloc")
	zid1 = request.form.get("zid1")
	zid2 = request.form.get("zid2")
	zid3 = request.form.get("zid3")
	zroute, zembed = zmaps.genroute(zid1, zid2, zid3)
	return render_template('index.html', zroute=zroute, zembed = zembed)

@app.route("/query")
def query():
	
        zid1 = request.args.get("zid1")
        zid2 = request.args.get("zid2")
        zid3 = request.args.get("zid3")
        zroute, zembed = zmaps.genroute(zid1, zid2, zid3)
        return render_template('index.html', zroute=zroute, zembed = zembed)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
