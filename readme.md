# CRD API with CORS support

This code implements a Flask RESTful API with Cross-Origin Resource Sharing (CORS) support. The API performs CRUD operations on a local JSON file data.json. The API has the following routes:

## RESTful API Routes

`/getlocs`: Route to handle GET requests and returns the contents of the data.json file as a JSON object.

`/postlocs`: Route to handle POST requests and adds the data from the request body to the data.json file.

`/dellocs`: Route to handle DELETE requests and removes the data from the request body from the data.json file.

## CORS Support

CORS support is implemented using the flask-cors library. The CORS class from the flask_cors module is initialized with the app object. The check function is defined to check the origin of the request. If the origin of the request is not equal to http://localhost:5000, the request is aborted with a 401 status code and an error message.

## Conclusion

This code provides a simple implementation of a Flask RESTful API with CORS support. The API performs basic CRUD operations on a local JSON file, and the CORS support ensures that only requests from the specified origin are processed. The code can be easily extended to perform more complex operations or to connect to a database instead of a local file.
