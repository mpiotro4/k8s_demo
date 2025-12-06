from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_PORT = int(os.getenv("APP_PORT", "8080"))
APP_MESSAGE = os.getenv("APP_MESSAGE", "default message")

@app.route("/")
def info():
    data = {
        "status": "ok",
        "message": APP_MESSAGE,
        "hostname": socket.gethostname(),
        "pod_ip": os.getenv("POD_IP"),
        "namespace": os.getenv("POD_NAMESPACE"),
        "node_name": os.getenv("NODE_NAME"),
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
