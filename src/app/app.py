from flask import Flask , request
import json
app = Flask(__name__)

@app.route('/api', methods=['POST','GET'])
def wm_api():
    message = 'Welcome to our demo API, here are the details of your request:'
    output = { 'message' : message  , 'Headers' : dict(request.headers) , 'Method' : str(request.method) , 'Body' : str(request.data,'utf8') }
    json_output = json.dumps(output, indent = 4)
    return json_output


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)