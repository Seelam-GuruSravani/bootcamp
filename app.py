from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import psutil

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Now you can access environment variables using os.getenv('KEY')
secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG') == 'True'

app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = debug_mode

@app.route('/ping')
def ping():
    return '200 OK'

@app.route('/healthz')
def healthz():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    return jsonify({'cpu_percent': cpu_percent, 'memory_percent': memory_percent})

if __name__ == '__main__':
    app.run(debug=True, port='8000', host='0.0.0.0')

