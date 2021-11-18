from flask import Flask
app=Flaskk(__name__)
@app.route("/")
def hello():
  return "Hello,World!"
