import logging
import time
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash,
    session,
)
from json import load
from json import dump
import os
import miner.miner as m

data = load(open("database/data.json"))
config = load(open("config.json"))
app = Flask(__name__)
app.secret_key = "187071677196f219bf777185d4740b0bcc45094f90e55a39af7c2bb75c17c46a"
log = logging.getLogger("werkzeug")
log.disabled = True
app.logger.disabled = True
status1 = False


@app.route("/login", methods=["GET", "POST"])
def login():
    if "api_key" in session:
        return redirect("/")
    else:
        if request.method == "POST":
            try:
                if not request.form["api_key"]:
                    return render_template(
                        "login.html", error="Please enter your api key"
                    )
                if request.form["api_key"] in data["keys"]:
                    session["api_key"] = request.form["api_key"]
                    return redirect("/")
                elif request.form["api_key"] not in data["keys"]:
                    return render_template("login.html", error="Invalid Credentials")
            except KeyError:
                return jsonify(
                    {"status": "failed", "reason": "No API key was provided"}
                )
    return render_template("login.html")


@app.route("/", methods=["POST", "GET"])
def miner():
    if "api_key" in session:
        return render_template("index.html")
    else:
        return redirect("/login")


@app.route("/receive", methods=["POST"])
def receive():
    if request.method == "POST":
        if request.headers["type"] == "json":
            try:
                config["data"] = request.json["data"]
                dump(fp=open("config.json", "w"), obj=config)
            except Exception as e:
                return jsonify({"status": "failed"})
        if request.headers["type"] == "config":
            try:
                return jsonify(config)
            except Exception as e:
                return jsonify({"reason": str(e)})

    return jsonify({"status": "success"})


@app.route("/send_file", methods=["POST"])
def send_file():
    if request.method == "POST":
        try:
            if request.headers["type"] == "token":
                config["authorization"] = request.json
                dump(obj=config, fp=open("config.json", "w"))
                return jsonify({"status": "success"})
            elif request.headers["type"] == "channel":
                config["channel"] = request.json
                dump(obj=config, fp=open("config.json", "w"))
                return jsonify({"status": "success"})
            elif request.headers["type"] == "commands":
                config["commands"] = request.json["commands"]
                dump(obj=config, fp=open("config.json", "w"))
                return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"reason": str(e)})


@app.route("/logout")
def logout():
    session.pop("api_key", None)
    return redirect("/login")


@app.route("/signal", methods=["POST"])
def start():
    if "api_key" in session:
        if request.method == "POST":
            if request.json["type"] == 2:
                global status1
                try:
                    if not status1:
                        x = m.StartMiners()
                        x.start_client(request.json["number"])
                        status1 = True
                        x.run_forever()
                    else:
                        return jsonify({"status": "error", "reason": "already running"})
                except Exception as e:
                    return jsonify({"reason": str(e)})
            elif request.json["type"] == 1:
                if status1:
                    file = open("./logs.log", "w")
                    file.write(" ")
                    status1 = False
                    os._exit(0)
                else:
                    return jsonify({"reason": "Not running"})


@app.route("/status", methods=["GET"])
def status():
    if "api_key" in session:
        try:
            return jsonify({"status": status1})
        except:
            pass


@app.route("/logs", methods=["GET"])
def logs():
    if "api_key" in session:
        try:
            file = open("logs.log", "r")
            return file.read()
        except FileNotFoundError:
            file = open("logs.log", "w")
            return ""


if "__main__" == __name__:
    print("Running on 127.0.0.1:5000")
    app.run(host="localhost", port=5000)
