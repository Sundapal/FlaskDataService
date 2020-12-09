
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

data = [
{"MarketCodeName":"LKF", "WorkWeek":"202101", "Yield":"96.77", "Volume":"212000"},
{"MarketCodeName":"LKF", "WorkWeek":"202102", "Yield":"96.77", "Volume":"423000"},
{"MarketCodeName":"LKF", "WorkWeek":"202103", "Yield":"94.01", "Volume":"344000"},
{"MarketCodeName":"LKF", "WorkWeek":"202104", "Yield":"95.48", "Volume":"453000"},
{"MarketCodeName":"LKF", "WorkWeek":"202105", "Yield":"95.30", "Volume":"323000"},
{"MarketCodeName":"LKF", "WorkWeek":"202106", "Yield":"95.77", "Volume":"425000"},
{"MarketCodeName":"LKF", "WorkWeek":"202107", "Yield":"96.20", "Volume":"429000"},
{"MarketCodeName":"LKF", "WorkWeek":"202108", "Yield":"90.11", "Volume":"366000"},
{"MarketCodeName":"LKF", "WorkWeek":"202109", "Yield":"95.47", "Volume":"413000"},
{"MarketCodeName":"LKF", "WorkWeek":"202110", "Yield":"96.62", "Volume":"455000"},
{"MarketCodeName":"LKF", "WorkWeek":"202111", "Yield":"95.22", "Volume":"414000"},
{"MarketCodeName":"LKF", "WorkWeek":"202112", "Yield":"96.87", "Volume":"362000"},
]

@app.route('/yield', methods=['GET'])
def getData():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost',port=60358)