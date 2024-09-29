from flask import Flask, render_template
from Fraud_Detection.Logger import logging

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return "Hello World"
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    app.run()