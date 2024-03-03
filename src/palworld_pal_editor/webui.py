import os
from pathlib import Path
import sys
import threading
import webbrowser
from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash
from palworld_pal_editor.api.util import reply

from palworld_pal_editor.config import Config
from palworld_pal_editor.api import *
from palworld_pal_editor.utils import LOGGER

BASE_PATH = Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else Path(__file__).parent

app = Flask(__name__, static_folder=BASE_PATH / "webui", static_url_path='/')
app.register_blueprint(player_blueprint, url_prefix='/api/player')
app.register_blueprint(pal_blueprint, url_prefix='/api/pal')
app.register_blueprint(save_blueprint, url_prefix='/api/save')
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
jwt = JWTManager(app)

@app.route('/image/<icon_type>/<filename>')
def serve_image(icon_type, filename):
    image_path = BASE_PATH / 'assets/icons' / icon_type / f"{filename}.png"
    if os.path.exists(image_path):
        directory = os.path.dirname(image_path)
        filename = os.path.basename(image_path)
        return send_from_directory(directory, filename)
    else:
        return "Image not found", 404


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(f"{app.static_folder}/{path}"):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    return reply(status=2, msg="Invalid Token: " + error_string), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return reply(status=2, msg="Token has expired"), 401

@jwt.unauthorized_loader
def missing_token_callback(error_string):
    return reply(status=2, msg="Authorization header missing"), 401


def main():
    Config._password_hash = generate_password_hash(Config.password or "")
    if Config.mode == "web" and not Config.debug:
        try:
            threading.Timer(3, lambda: webbrowser.open(f"http://127.0.0.1:{Config.port}") ).start()
        except:
            LOGGER.info("Failed to launch browser.")
    host = '0.0.0.0' if Config.mode == "web" else "127.0.0.1"
    if Config.debug:
        app.run(use_reloader=True, port=Config.port, threaded=True)
    else:
        from waitress import serve
        LOGGER.info(f"LISTENING ON {host}:{Config.port}.")
        serve(app, host=host, port=Config.port, threads=6)