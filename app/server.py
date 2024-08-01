from flask import Flask, send_from_directory, redirect, request
from werkzeug.serving import make_server
import logging
from tools import href

server = Flask(__name__)

@server.route('/login')
def login():
    return redirect(f'/login/index.html?{request.query_string.decode("utf-8")}')

@server.route('/login/<path:name>')
def login_path(name):
    return send_from_directory(href('templates', 'login'), name)

def start_server(stop_event):
    server_instance = make_server('0.0.0.0', 81, server)
    
    try:
        logging.info('Server is running on http://localhost:81')
        while not stop_event.is_set():
            server_instance.handle_request()
    except Exception as e:
        logging.error(f'Error running server: {e}')
    finally:
        logging.info('Stopping server...')
        server_instance.server_close()
