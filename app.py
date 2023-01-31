# Importing necessary modules
from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS, cross_origin
import json

# Initializing Flask app
app = Flask(__name__)

# URL to check against during CORS check
mainurl = 'http://localhost:5000'

# Enabling Cross Origin Resource Sharing (CORS)
CORS(app)

# Function to check for allowed origins


@app.before_request
def check():
    # Check if request origin is not equal to mainurl
    if request.origin != mainurl:
        # Prepare error message as JSON
        error_message = json.dumps(
            {'Data': 'Sorry this site is not supported'})
        # Abort the request with 401 status and error message
        abort(Response(error_message, 401))

# Route to handle GET requests


@app.route('/getlocs', methods=['GET'])
def getreq():
    # Open data.json file in read mode
    with open('data.json', 'r') as file:
        # Load data from the file
        file_data = json.load(file)
    # Return file data as JSON
    return jsonify(file_data)

# Route to handle POST requests


@app.route('/postlocs', methods=['POST'])
def postreq():
    # Open data.json file in read-write mode
    with open('data.json', 'r+') as file:
        # Load data from the file
        file_data = json.load(file)
        # If request contains JSON data
        if request.json is not None:
            # Get JSON data from the request
            json_str = request.json
            # Append the new data to file data
            file_data[0]["data"].append(json_str)
            # Move file pointer to the start of the file
            file.seek(0)
            # Dump file data to the file
            json.dump(file_data, file, indent=4)
            # Print the new data
            print(json_str)
    # Return file data as JSON
    return jsonify(file_data)

# Route to handle DELETE requests


@app.route('/dellocs', methods=['DELETE'])
def delreq():
    # Open data.json file in read-write mode
    with open('data.json', 'r+') as file:
        # Load data from the file
        file_data = json.load(file)
        # If request contains JSON data
        if request.json is not None:
            # Get JSON data from the request
            json_str = request.json
            # Remove the data from file data
            file_data[0]["data"].remove(json_str)
            # Move file pointer to the start of the file
            file.seek(0)
            # Clear the contents of the file
            open("data.json", "w").close()
            # Dump file data to the file
            json.dump(file_data, file, indent=4)
    # Return file data as JSON
    return jsonify(file_data)


# Entry point for the program
if __name__ == "__main__":
    # Start the code
    app.run()
