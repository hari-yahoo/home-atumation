from flask import Flask
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
  control(id, "start")


@app.route("/stop/<int:id>")
def stop(id):
  control(id, "stop")


def control(pin, operation):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(pin, GPIO.OUT)
  if (operation == "start"):
    GPIO.output(pin, GPIO.HIGH)
  else:
    GPIO.output(pin, GPIO.LOW)
    
