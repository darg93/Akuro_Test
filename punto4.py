from flask import Flask, request
from flask import jsonify


app = Flask(__name__)



@app.route('/procesingEndpoint', methods=['GET'])
def index():
    id = int(request.args['id'])
    mount = int(request.args['mount'])
    
    return jsonify(success='OK',
                   total=mount*id/4)

