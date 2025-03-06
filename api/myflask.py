from flask import Flask


app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"1":2,"3":4}

app.run()