import socket

from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def fetch_host_details():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_name, host_ip


@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'


@app.route('/health')
def health():
    return jsonify({'status': 'UP'})


@app.route('/details')
def details():
    host_name, host_ip = fetch_host_details()
    return render_template('index.html', host_name=host_name, host_ip=host_ip)
