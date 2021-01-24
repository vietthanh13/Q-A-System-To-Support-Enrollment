import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request,  jsonify

# ######## INIT FLASK

app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'] )
@cross_origin(origin='*')
def home():
    return render_template('index.html')


# Bật Backend ở cổng 6868
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')