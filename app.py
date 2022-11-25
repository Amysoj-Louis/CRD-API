from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)

#####################################################################
# mainurl = 'http://localhost:5000'
# CORS(app)


# @app.before_request
# def check():
#     if request.origin != mainurl:
#         error_message = json.dumps({'Data': 'Sorry this site is not supported'})
#         abort(Response(error_message, 401))
######################################################################

@app.route('/getlocs', methods=['GET'])
def getreq():
    with open('data.json', 'r') as file:
        file_data = json.load(file)
    return jsonify(file_data)


@app.route('/postlocs', methods=['POST'])
def postreq():
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        if request.json is not None:
            json_str = request.json
            file_data[0]["data"].append(json_str)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            print(json_str)
    return jsonify(file_data)


@app.route('/dellocs', methods=['DELETE'])
def delreq():
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        if request.json is not None:
            json_str = request.json
            file_data[0]["data"].remove(json_str)
            file.seek(0)
            open("data.json", "w").close()
            json.dump(file_data, file, indent=4)
    return jsonify(file_data)


if __name__ == "__main__":
    app.run()
