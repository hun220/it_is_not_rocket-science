import threading
from threading import Thread
from flask import Flask, render_template
import gui
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    Thread(target = app.run).start()
    Thread(target = gui.main).start()