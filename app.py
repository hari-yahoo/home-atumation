from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/devices")
def devices():
  return render_template('index.html')


@app.route("/start/<int:id>")
def start(id):
  status = control(id, "start")
  return f"Status is {status}"

@app.route("/stop/<int:id>")
def stop(id):
  status = control(id, "stop")
  return f"Status is {status}"

@app.route("/status/<int:id>")
def status(id):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(id, GPIO.OUT)

  res = {
    "status" : GPIO.input(id)
  }
  return jsonify(res)

def control(pin, operation):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pin, GPIO.OUT)
  if (operation == "start"):
    GPIO.output(pin, GPIO.HIGH)
  else:
    GPIO.output(pin, GPIO.LOW)
  return GPIO.input(pin)
    
